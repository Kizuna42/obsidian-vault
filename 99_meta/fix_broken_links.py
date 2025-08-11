#!/usr/bin/env python3
"""
Broken Links Repair Script for Obsidian Vault
Fixes URL-encoded links and broken references
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

def fix_encoded_links(content):
    """Fix URL-encoded wiki links"""
    # Pattern to find [[encoded_link]]
    pattern = r'\[\[([^]]+)\]\]'
    
    def decode_link(match):
        link = match.group(1)
        # Decode URL encoding
        decoded = unquote(link)
        return f"[[{decoded}]]"
    
    return re.sub(pattern, decode_link, content)

def fix_template_links(content):
    """Remove template-related broken links"""
    # Remove template placeholder links
    patterns = [
        r'\[\[\{\{date:YYYY-MM-DD\|%j [-+] \d+\}\}\]\]',
        r'\[\[\{\{title\}\}\]\]',  
        r'\[\[\{\{.*?\}\}\]\]',
        r'\[\[\\\\1\]\]',  # Regex artifacts
        r'\[\[\^\]\]',    # Caret symbols
        r'\[\[link\]\]',  # Generic placeholder links
        r'\[\[link\.md\]\]',  # Generic placeholder md links
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content)
    
    return content

def fix_broken_links_in_file(file_path):
    """Fix broken links in a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_encoded_links(content)
        content = fix_template_links(content)
        
        # Only write if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        
    return False

def fix_all_broken_links(vault_path):
    """Fix broken links in all markdown files"""
    vault_path = Path(vault_path)
    fixed_count = 0
    
    for root, dirs, files in os.walk(vault_path):
        # Skip .git and .obsidian directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian']]
        
        for filename in files:
            if filename.endswith('.md'):
                file_path = Path(root) / filename
                if fix_broken_links_in_file(file_path):
                    fixed_count += 1
                    print(f"Fixed links in: {file_path.relative_to(vault_path)}")
    
    print(f"\nFixed broken links in {fixed_count} files")
    return fixed_count

if __name__ == "__main__":
    vault_path = "/Users/kizuna/Obsidian/Vault"
    fix_all_broken_links(vault_path)