#!/usr/bin/env python3
"""
UUID Cleanup Script for Obsidian Vault
Removes UUID suffixes from filenames and updates internal links
"""

import os
import re
import shutil
from pathlib import Path

def clean_filename(filename):
    """Remove UUID patterns from filename"""
    # Pattern for UUID: 8-4-4-4-12 hex characters
    uuid_pattern = r'\s+[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
    # Pattern for short hex suffixes
    hex_pattern = r'\s+[a-f0-9]{32}'
    
    cleaned = re.sub(uuid_pattern, '', filename, flags=re.IGNORECASE)
    cleaned = re.sub(hex_pattern, '', cleaned, flags=re.IGNORECASE)
    
    return cleaned.strip()

def update_markdown_links(file_path, old_name, new_name):
    """Update markdown internal links in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update [[old_name]] style links
        old_link_pattern = f"\\[\\[{re.escape(old_name)}\\]\\]"
        new_link = f"[[{new_name}]]"
        updated_content = re.sub(old_link_pattern, new_link, content)
        
        # Update [text](old_name) style links  
        old_md_pattern = f"\\]\\({re.escape(old_name)}\\)"
        new_md_link = f"]({new_name})"
        updated_content = re.sub(old_md_pattern, new_md_link, updated_content)
        
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
                
                for _, info in renamed_files.items():
                    if update_markdown_links(file_path, info['old_name'], info['new_name']):
                        updated_files += 1
                        break
    
    print(f"Updated links in {updated_files} markdown files")
    return len(renamed_files), updated_files

if __name__ == "__main__":
    vault_path = "/Users/kizuna/Obsidian/Vault"
    renamed_count, updated_count = cleanup_uuid_files(vault_path)
    print(f"\nCleanup completed:")
    print(f"- Renamed {renamed_count} files") 
    print(f"- Updated {updated_count} markdown files")