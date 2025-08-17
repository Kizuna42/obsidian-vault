#!/usr/bin/env python3
"""
UUID Cleanup Script for Obsidian Vault
Removes UUID suffixes from filenames and updates internal links
"""

import os
import re
import shutil
from pathlib import Path
import argparse
from urllib.parse import quote, unquote

UUID_PATTERN = r"\s+[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
HEX32_PATTERN = r"\s+[a-f0-9]{32}"


def clean_name_component(name: str) -> str:
    cleaned = re.sub(UUID_PATTERN, '', name, flags=re.IGNORECASE)
    cleaned = re.sub(HEX32_PATTERN, '', cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


def clean_filename(filename):
    """Remove UUID patterns from filename"""
    return clean_name_component(filename)


def update_markdown_links_in_content(content: str, replacements: list[tuple[str, str]]) -> str:
    updated = content
    for old_rel, new_rel in replacements:
        old_raw = old_rel
        new_raw = new_rel
        old_enc = quote(old_rel, safe='/._-() ')
        new_enc = quote(new_rel, safe='/._-() ')
        # [[old]]
        updated = re.sub(r"\\[\\[" + re.escape(old_raw) + r"\\]\\]", f"[[{new_raw}]]", updated)
        updated = re.sub(r"\\[\\[" + re.escape(old_enc) + r"\\]\\]", f"[[{new_enc}]]", updated)
        # [[old|alias]]
        updated = re.sub(r"\\[\\[" + re.escape(old_raw) + r"\|", f"[[{new_raw}|", updated)
        updated = re.sub(r"\\[\\[" + re.escape(old_enc) + r"\|", f"[[{new_enc}|", updated)
        # ](old)
        updated = re.sub(r"\]\(" + re.escape(old_raw) + r"\)", f"]({new_raw})", updated)
        updated = re.sub(r"\]\(" + re.escape(old_enc) + r"\)", f"]({new_enc})", updated)
    return updated


def update_markdown_links(file_path: Path, replacements: list[tuple[str, str]]):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        updated_content = update_markdown_links_in_content(content, replacements)
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
    return False


def cleanup_uuid_files(vault_path):
    """Main function to clean up UUID filenames"""
    vault_path = Path(vault_path)
    renamed_files = {}
    
    # First pass: identify files to rename
    for root, dirs, files in os.walk(vault_path):
        root_path = Path(root)
        
        for filename in files:
            if filename.startswith('.'):
                continue
                
            clean_name = clean_filename(filename)
            if clean_name != filename and clean_name.strip():
                file_path = root_path / filename
                new_path = root_path / clean_name
                
                # Avoid conflicts
                if new_path.exists():
                    clean_name = f"{clean_name.stem}_cleaned{clean_name.suffix}"
                    new_path = root_path / clean_name
                
                renamed_files[str(file_path)] = {
                    'old_name': filename,
                    'new_name': clean_name,
                    'new_path': new_path
                }
    
    print(f"Found {len(renamed_files)} files to rename")
    
    # Second pass: rename files
    for old_path, info in renamed_files.items():
        try:
            old_file = Path(old_path)
            if old_file.exists():
                shutil.move(old_path, info['new_path'])
                print(f"Renamed: {info['old_name']} → {info['new_name']}")
        except Exception as e:
            print(f"Error renaming {old_path}: {e}")
    
    # Third pass: update links in markdown files
    updated_files = 0
    for root, dirs, files in os.walk(vault_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = Path(root) / filename
                
                # Prepare replacements for this file
                replacements = []
                for _, info in renamed_files.items():
                    replacements.append((info['old_name'], info['new_name']))
                
                if update_markdown_links(file_path, replacements):
                    updated_files += 1
    
    print(f"Updated links in {updated_files} markdown files")
    return len(renamed_files), updated_files

if __name__ == "__main__":
    vault_path = "/Users/kizuna/Obsidian/Vault"
    renamed_count, updated_count = cleanup_uuid_files(vault_path)
    print(f"\nCleanup completed:")
    print(f"- Renamed {renamed_count} files") 
    print(f"- Updated {updated_count} markdown files")