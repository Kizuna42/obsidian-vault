#!/usr/bin/env python3
"""
Link Integrity Check for Obsidian Vault
Finds and reports broken internal links
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_internal_links(content):
    """Extract all internal links from markdown content"""
    # Find [[link]] style links
    wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    # Find [text](link.md) style links to .md files
    md_links = re.findall(r'\]\(([^)]+\.md)\)', content)
    
    return wiki_links + md_links

def find_all_md_files(vault_path):
    """Get all markdown files in the vault"""
    md_files = {}
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                full_path = Path(root) / file
                # Store both filename and full path
                md_files[file] = full_path
                # Also store without .md extension for wiki links
                name_without_ext = file[:-3]
                md_files[name_without_ext] = full_path
    
    return md_files

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
                        clean_link = link.split('#')[0].strip()
                        
                        # Skip empty links
                        if not clean_link:
                            continue
                            
                        # Check if the target file exists
                        if clean_link not in md_files:
                            # Try with .md extension if not already there
                            if not clean_link.endswith('.md'):
                                alt_link = clean_link + '.md'
                                if alt_link not in md_files:
                                    broken_links[str(file_path)].append(link)
                            else:
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