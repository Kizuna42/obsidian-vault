#!/usr/bin/env python3
"""
Link Integrity Check for Obsidian Vault
Finds and reports broken internal links
"""

import os
import re
from urllib.parse import unquote
from pathlib import Path
from collections import defaultdict

def extract_internal_links(content):
    """Extract all internal links from markdown content"""
    # Find [[link]] style links
    wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    # Find [text](link.md) style links to .md files
    md_links = re.findall(r'\]\(([^)]+\.md)\)', content)
    
    return wiki_links + md_links


def build_md_index(vault_path: Path):
    """Index markdown files by multiple keys for robust resolution.
    Keys include:
    - filename (with and without .md)
    - vault-relative path with forward slashes (with and without .md)
    - percent-encoded variants of the above
    """
    md_index = {}
    for root, _, files in os.walk(vault_path):
        root_path = Path(root)
        for file in files:
            if not file.endswith('.md'):
                continue
            full_path = root_path / file
            rel_path = full_path.relative_to(vault_path)
            rel_str = str(rel_path).replace('\\', '/')
            name_with_ext = file
            name_without_ext = file[:-3]

            # Base name keys
            md_index[name_with_ext] = full_path
            md_index[name_without_ext] = full_path

            # Relative path keys
            rel_no_ext = rel_str[:-3] if rel_str.lower().endswith('.md') else rel_str
            md_index[rel_str] = full_path
            md_index[rel_no_ext] = full_path

            # Percent-encoded variants
            # Note: store encoded keys to match links that are URL-encoded in notes
            try:
                from urllib.parse import quote
                encoded_rel = quote(rel_str, safe='/._-() ')
                encoded_rel_no_ext = quote(rel_no_ext, safe='/._-() ')
                encoded_name_with_ext = quote(name_with_ext, safe='/._-() ')
                encoded_name_without_ext = quote(name_without_ext, safe='/._-() ')
                md_index[encoded_rel] = full_path
                md_index[encoded_rel_no_ext] = full_path
                md_index[encoded_name_with_ext] = full_path
                md_index[encoded_name_without_ext] = full_path
            except Exception:
                pass

    return md_index

def find_all_md_files(vault_path):
    """Get all markdown files in the vault, indexed by multiple keys."""
    return build_md_index(Path(vault_path))

def check_link_integrity(vault_path):
    """Check for broken internal links"""
    vault_path = Path(vault_path)
    md_files = find_all_md_files(vault_path)
    broken_links = defaultdict(list)
    
    print(f"Found {len(set(md_files.values()))} markdown files in vault")
    
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    links = extract_internal_links(content)
                    
                    for link in links:
                        # Clean the link (remove anchors, etc.)
                        # Support alias syntax [[target|alias]]
                        link_body = link.split('|', 1)[0]
                        clean_link = link_body.split('#')[0].strip()
                        if not clean_link:
                            continue
                        decoded_link = unquote(clean_link)
                        
                        # Resolution order: decoded exact, decoded with .md, raw exact, raw with .md
                        candidates = [
                            decoded_link,
                            decoded_link if decoded_link.lower().endswith('.md') else decoded_link + '.md',
                            clean_link,
                            clean_link if clean_link.lower().endswith('.md') else clean_link + '.md',
                        ]

                        # Relative path resolution from the current file's directory
                        try:
                            rel_base = file_path.parent.relative_to(vault_path)
                            rel_base_str = str(rel_base).replace('\\', '/')
                            for base in (rel_base_str, str(file_path.parent)):
                                if not base:
                                    continue
                                # Compose and normalize
                                for candidate in (decoded_link, clean_link):
                                    joined = f"{base}/{candidate}" if base else candidate
                                    joined = joined.replace('//', '/')
                                    # Remove any leading './'
                                    if joined.startswith('./'):
                                        joined = joined[2:]
                                    # Add both with and without .md
                                    if joined not in candidates:
                                        candidates.append(joined)
                                    if not joined.lower().endswith('.md'):
                                        with_md = joined + '.md'
                                        if with_md not in candidates:
                                            candidates.append(with_md)
                        except Exception:
                            pass

                        if not any(candidate in md_files for candidate in candidates):
                            broken_links[str(file_path)].append(link)
                    
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return broken_links

def generate_report(broken_links):
    """Generate a report of broken links"""
    if not broken_links:
        print("✅ No broken internal links found!")
        return
    
    print(f"❌ Found broken links in {len(broken_links)} files:")
    print("=" * 60)
    
    for file_path, links in broken_links.items():
        rel_path = file_path.replace('/Users/kizuna/Obsidian/Vault/', '')
        print(f"\n📄 {rel_path}")
        for link in links:
            print(f"   🔗 [[{link}]]")
    
    print(f"\n📊 Summary: {sum(len(links) for links in broken_links.values())} broken links total")

if __name__ == "__main__":
    vault_path = "/Users/kizuna/Obsidian/Vault"
    broken_links = check_link_integrity(vault_path)
    generate_report(broken_links)