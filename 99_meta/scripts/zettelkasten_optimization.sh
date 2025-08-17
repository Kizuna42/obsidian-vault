#!/bin/bash

# =============================================================================
# Zettelkasten & Areas Directory Optimization Script
# =============================================================================

set -e  # Exit on any error

# Configuration
DRY_RUN=${DRY_RUN:-true}
VAULT_ROOT="/Users/kizuna/Obsidian/Vault"
LOG_FILE="$VAULT_ROOT/99_meta/optimization_log_$(date +%Y%m%d_%H%M%S).log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
}

# Execution wrapper
execute() {
    local cmd="$1"
    local description="$2"
    
    if [ "$DRY_RUN" = true ]; then
        echo -e "${BLUE}[DRY-RUN]${NC} $description"
        echo "    $cmd"
    else
        log "$description"
        eval "$cmd"
    fi
}

# Create directory if it doesn't exist
create_dir() {
    local dir_path="$1"
    if [ ! -d "$dir_path" ]; then
        execute "mkdir -p '$dir_path'" "Creating directory: $dir_path"
    fi
}

# =============================================================================
# PHASE 0: BACKUP AND BRANCH CREATION
# =============================================================================

phase0_backup() {
    log "=== Phase 0: Backup and Branch Creation ==="
    
    cd "$VAULT_ROOT"
    
    # Create backup commit
    execute "git add -A" "Staging all current changes"
    execute "git commit -m 'backup: pre-zettelkasten-optimization $(date)'" "Creating backup commit"
    
    # Create optimization branch
    local branch_name="zettelkasten-optimization-$(date +%Y%m%d)"
    execute "git checkout -b '$branch_name'" "Creating optimization branch: $branch_name"
    
    log "Backup completed successfully"
}

# =============================================================================
# PHASE 1: CLEANUP EMPTY AND MISPLACED FILES
# =============================================================================

phase1_cleanup() {
    log "=== Phase 1: Empty Files Cleanup and Misplacement Fix ==="
    
    cd "$VAULT_ROOT"
    
    # Files to delete (empty or near-empty)
    local files_to_delete=(
        "02_zettelkasten/insights/global-challenges/Notion使い方.md"
        "20_areas/business/home-tutor/土手ひまり.md"
        "20_areas/business/home-tutor/廣瀬こう.md"
        "20_areas/business/home-tutor/廣瀬りょう.md"
        "20_areas/programming/archive/AI経済社会学/第1回.md"
        "20_areas/programming/archive/AI経済社会学/第3回.md"
        "20_areas/programming/archive/AI経済社会学/第4回.md"
        "20_areas/programming/archive/AI経済社会学/第5回.md"
        "20_areas/programming/archive/AI経済社会学/第7回.md"
        "20_areas/education/academy/そうだったのか日本/藤沢.md"
    )
    
    for file in "${files_to_delete[@]}"; do
        if [ -f "$file" ]; then
            execute "git rm '$file'" "Deleting empty file: $file"
        else
            warning "File not found: $file"
        fi
    done
    
    # Create new directory structure for insights
    create_dir "02_zettelkasten/insights/business"
    create_dir "02_zettelkasten/insights/personal"
    create_dir "02_zettelkasten/insights/technical"
    create_dir "02_zettelkasten/index"
    create_dir "20_areas/business/startup"
    
    # Move misplaced files
    local moves=(
        "02_zettelkasten/insights/global-challenges/Untitled.md:02_zettelkasten/concepts/2025-08-11-metaverse-keywords.md"
        "02_zettelkasten/insights/global-challenges/信仰.md:02_zettelkasten/insights/personal/2025-08-11-faith-reflection.md"
        "02_zettelkasten/insights/起業アイデアの候補.md:20_areas/business/startup/startup-ideas-candidates.md"
        "20_areas/business/startup-basic-plan.md:20_areas/business/startup/basic-plan.md"
    )
    
    for move in "${moves[@]}"; do
        local old_path="${move%%:*}"
        local new_path="${move##*:}"
        if [ -f "$old_path" ]; then
            execute "git mv '$old_path' '$new_path'" "Moving: $old_path → $new_path"
        else
            warning "Source file not found: $old_path"
        fi
    done
    
    log "Phase 1 cleanup completed"
}

# =============================================================================
# PHASE 2: IDEA FLASH GLOBAL CONSOLIDATION
# =============================================================================

phase2_global_challenges() {
    log "=== Phase 2: IDEA FLASH GLOBAL Consolidation ==="
    
    cd "$VAULT_ROOT"
    
    local source_dir="02_zettelkasten/insights/global-challenges/世界の課題リスト【IDEA FLASH GLOBAL】/【IDEA FLASH GLOBAL】"
    local output_file="02_zettelkasten/insights/global-challenges/2025-08-11-global-challenges-database.md"
    
    if [ ! -d "$source_dir" ]; then
        error "Source directory not found: $source_dir"
        return 1
    fi
    
    # Create consolidated file
    if [ "$DRY_RUN" = true ]; then
        echo -e "${BLUE}[DRY-RUN]${NC} Creating consolidated global challenges database"
        echo "    Output: $output_file"
        echo "    Source files: $(find "$source_dir" -name "*.md" | wc -l) markdown files"
    else
        log "Creating consolidated global challenges database: $output_file"
        
        # Create frontmatter and header
        cat > "$output_file" << 'EOF'
---
title: "Global Challenges Database"
created: 2025-08-11
updated: 2025-08-11
tags: [global-challenges, database, insights]
category: insight
status: active
zettel_id: 202508111200
aliases: [世界の課題リスト, IDEA FLASH GLOBAL]
related: []
---

# Global Challenges Database

This database consolidates 141 individual global challenge insights originally stored as separate files in the IDEA FLASH GLOBAL collection.

## Challenge Categories

EOF

        # Process all markdown files in the source directory
        local count=0
        for file in "$source_dir"/*.md; do
            if [ -f "$file" ]; then
                local filename=$(basename "$file" .md)
                echo "### $filename" >> "$output_file"
                echo "" >> "$output_file"
                
                # Extract content (skip title if it matches filename)
                tail -n +2 "$file" >> "$output_file"
                echo "" >> "$output_file"
                echo "---" >> "$output_file"
                echo "" >> "$output_file"
                
                ((count++))
            fi
        done
        
        log "Consolidated $count global challenge files into database"
    fi
    
    # Remove the original directory structure after consolidation
    if [ -d "$source_dir" ]; then
        execute "git rm -r '02_zettelkasten/insights/global-challenges/世界の課題リスト【IDEA FLASH GLOBAL】'" "Removing original IDEA FLASH GLOBAL directory structure"
    fi
    
    log "Phase 2 consolidation completed"
}

# =============================================================================
# PHASE 3: FRONTMATTER ADDITION
# =============================================================================

phase3_frontmatter() {
    log "=== Phase 3: Adding Frontmatter to Key Files ==="
    
    cd "$VAULT_ROOT"
    
    # Files that need frontmatter (high priority)
    local important_files=(
        "02_zettelkasten/insights/global-challenges/GPT4.md:concept"
        "02_zettelkasten/insights/global-challenges/2025.md:insight"
        "20_areas/business/home-tutor/概要.md:area"
        "20_areas/personal/Vision.md:area"
        "20_areas/personal/Life Strategy.md:area"
        "20_areas/programming/cpp-modules-workflow.md:area"
    )
    
    for file_info in "${important_files[@]}"; do
        local file_path="${file_info%%:*}"
        local category="${file_info##*:}"
        
        if [ -f "$file_path" ] && ! grep -q "^---" "$file_path"; then
            if [ "$DRY_RUN" = true ]; then
                echo -e "${BLUE}[DRY-RUN]${NC} Adding frontmatter to: $file_path (category: $category)"
            else
                # Create temporary file with frontmatter
                local temp_file=$(mktemp)
                local filename=$(basename "$file_path" .md)
                local created_date=$(date +%Y-%m-%d)
                
                cat > "$temp_file" << EOF
---
title: "$filename"
created: $created_date
updated: $created_date
tags: []
category: $category
status: active
zettel_id: $(date +%Y%m%d%H%M)
aliases: []
related: []
---

EOF
                # Append original content
                cat "$file_path" >> "$temp_file"
                
                # Replace original file
                mv "$temp_file" "$file_path"
                
                log "Added frontmatter to: $file_path"
            fi
        fi
    done
    
    log "Phase 3 frontmatter addition completed"
}

# =============================================================================
# PHASE 4: VALIDATION AND VERIFICATION
# =============================================================================

phase4_validation() {
    log "=== Phase 4: Validation and Verification ==="
    
    cd "$VAULT_ROOT"
    
    # Check for broken links (basic check)
    if [ "$DRY_RUN" = true ]; then
        echo -e "${BLUE}[DRY-RUN]${NC} Running link integrity check"
        echo "    Command: python3 99_meta/check_broken_links.py"
    else
        log "Running link integrity check"
        if [ -f "99_meta/check_broken_links.py" ]; then
            python3 99_meta/check_broken_links.py > "$VAULT_ROOT/99_meta/post_optimization_link_check.log"
            log "Link check completed - see post_optimization_link_check.log"
        else
            warning "Link checker script not found"
        fi
    fi
    
    # Count files before/after
    local insights_count=$(find "02_zettelkasten/insights" -name "*.md" 2>/dev/null | wc -l || echo 0)
    local areas_count=$(find "20_areas" -name "*.md" 2>/dev/null | wc -l || echo 0)
    
    log "File count after optimization:"
    log "  - 02_zettelkasten/insights: $insights_count files"
    log "  - 20_areas: $areas_count files"
    
    log "Phase 4 validation completed"
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    local phase=${1:-all}
    
    log "Starting Zettelkasten Optimization (DRY_RUN=$DRY_RUN)"
    log "Target directories: 02_zettelkasten/insights, 20_areas"
    
    case $phase in
        "backup"|"0")
            phase0_backup
            ;;
        "cleanup"|"1")
            phase1_cleanup
            ;;
        "consolidate"|"2")
            phase2_global_challenges
            ;;
        "frontmatter"|"3")
            phase3_frontmatter
            ;;
        "validate"|"4")
            phase4_validation
            ;;
        "all")
            phase0_backup
            phase1_cleanup
            phase2_global_challenges
            phase3_frontmatter
            phase4_validation
            ;;
        *)
            error "Unknown phase: $phase"
            echo "Usage: $0 [backup|cleanup|consolidate|frontmatter|validate|all]"
            exit 1
            ;;
    esac
    
    if [ "$DRY_RUN" = true ]; then
        echo ""
        echo -e "${YELLOW}=== DRY RUN COMPLETED ===${NC}"
        echo "To execute for real, run: DRY_RUN=false $0 $phase"
    else
        log "Optimization phase '$phase' completed successfully"
        log "Log file: $LOG_FILE"
    fi
}

# Run main function with all arguments
main "$@"