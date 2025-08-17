#!/usr/bin/env python3
"""
Enhanced UUID Cleanup Script for Obsidian Vault
Handles various UUID patterns including space-prefixed UUIDs
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote, unquote

def clean_filename(filename):
    """Remove various UUID patterns from filename"""
    # Pattern 1: Space + UUID (8-4-4-4-12)
    uuid_pattern1 = r'\s+[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
    # Pattern 2: Space + 32 hex chars  
    hex32_pattern = r'\s+[a-f0-9]{32}'
    
    cleaned = re.sub(uuid_pattern1, '', filename, flags=re.IGNORECASE)
    cleaned = re.sub(hex32_pattern, '', cleaned, flags=re.IGNORECASE)
    
    return cleaned.strip()

def update_markdown_links(file_path, replacements):
    """Update markdown internal links in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = content
        changed = False
        
        for old_name, new_name in replacements:
            if old_name != new_name:
                # Update [[old_name]] style links
                old_link_pattern = f"\\[\\[{re.escape(old_name)}\\]\\]"
                new_link = f"[[{new_name}]]"
                if re.search(old_link_pattern, updated_content):
                    updated_content = re.sub(old_link_pattern, new_link, updated_content)
                    changed = True
                
                # Update [text](old_name.md) style links
                old_md_pattern = f"\\]\\({re.escape(old_name)}\\.md\\)"
                new_md_link = f"]({new_name}.md)"
                if re.search(old_md_pattern, updated_content):
                    updated_content = re.sub(old_md_pattern, new_md_link, updated_content)
                    changed = True
        
        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
    
    return False

def cleanup_uuid_files_and_folders(vault_path):
    """Main function to clean up UUID filenames and folder names"""
    vault_path = Path(vault_path)
    renames = []  # (old_path, new_path, old_name, new_name)
    
    # Collect all items (files and folders) to rename
    for root, dirs, files in os.walk(vault_path, topdown=False):
        root_path = Path(root)
        
        # Process files first
        for filename in files:
            if filename.startswith('.'):
                continue
                
            clean_name = clean_filename(filename)
            if clean_name != filename and clean_name.strip():
                file_path = root_path / filename
                new_path = root_path / clean_name
                
                # Avoid conflicts by adding suffix
                counter = 1
                original_clean = clean_name
                while new_path.exists():
                    name_part, ext = os.path.splitext(original_clean)
                    clean_name = f"{name_part}_cleaned{counter}{ext}"
                    new_path = root_path / clean_name
                    counter += 1
                
                renames.append((file_path, new_path, filename, clean_name))
        
        # Process directories
        for dirname in dirs:
            clean_name = clean_filename(dirname)
            if clean_name != dirname and clean_name.strip():
                dir_path = root_path / dirname
                new_path = root_path / clean_name
                
                # Avoid conflicts
                counter = 1
                original_clean = clean_name
                while new_path.exists():
                    clean_name = f"{original_clean}_cleaned{counter}"
                    new_path = root_path / clean_name
                    counter += 1
                
                renames.append((dir_path, new_path, dirname, clean_name))
    
    print(f"Found {len(renames)} items to rename")
    
    # Perform renames
    renamed_count = 0
    for old_path, new_path, old_name, new_name in renames:
        try:
            if old_path.exists():
                shutil.move(str(old_path), str(new_path))
                print(f"Renamed: {old_name} → {new_name}")
                renamed_count += 1
        except Exception as e:
            print(f"Error renaming {old_path}: {e}")
    
    # Update links in markdown files
    link_replacements = [(old_name, new_name) for _, _, old_name, new_name in renames if old_name.endswith('.md')]
    updated_files = 0
    
    for root, dirs, files in os.walk(vault_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = Path(root) / filename
                if update_markdown_links(file_path, link_replacements):
                    updated_files += 1
    
    print(f"\nCleanup completed:")
    print(f"- Renamed {renamed_count} items")
    print(f"- Updated links in {updated_files} markdown files")
    
    return renamed_count, updated_files

if __name__ == "__main__":
    vault_path = "/Users/kizuna/Obsidian/Vault"
    renamed_count, updated_count = cleanup_uuid_files_and_folders(vault_path)