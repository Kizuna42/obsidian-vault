# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Obsidian personal knowledge vault** organized using the PARA method (Projects, Areas, Resources, Archives). The vault contains personal notes, literature summaries, daily logs, and project documentation in markdown format.

## Repository Structure

- `00_inbox/` - Temporary notes and unprocessed content
- `01_daily/` - Daily notes and logs (format: YYYY-MM-DD.md)
- `02_zettelkasten/` - Atomic notes and knowledge connections
  - `concepts/` - Core concepts and ideas
  - `insights/` - Discovered insights and observations
    - `business/` - Business-related insights
    - `personal/` - Personal development insights
    - `technical/` - Technical insights
    - `global-challenges/` - Global challenges database and insights
  - `connections/` - Relationship mappings between concepts
  - `index/` - Index files and structured overviews
- `10_projects/` - Active project files with deadlines
- `20_areas/` - Ongoing areas of responsibility
  - `business/` - Business analysis and planning materials
    - `home-tutor/` - Home tutoring business documentation
  - `education/` - Learning and educational materials
  - `personal/` - Personal development and goals
  - `programming/` - Software development and learning materials
  - `technical/` - Technical reports and documentation
- `30_resources/` - Reference materials for future use
  - `literature/` - Book summaries and research notes
  - `references/` - Technical references and documentation
  - `templates/` - Note templates for consistent formatting (Daily, Project, Literature, Zettelkasten)
- `90_archive/` - Completed or inactive content
  - `duplicates_20250811/` - Archived duplicate files
  - `ingested_exports_20250811/` - Archived imported content
- `99_meta/` - Vault maintenance scripts and documentation
- `.obsidian/` - Obsidian app configuration and plugins

## Obsidian Configuration

### Active Plugins
- **dataview** - Database-like queries for notes
- **excalibrain** - Visual knowledge graph
- **obsidian-excalidraw-plugin** - Drawing and diagramming
- **recent-files-obsidian** - Recent files management
- **templater-obsidian** - Advanced templating
- **omnisearch** - Enhanced search functionality
- **typing-assistant** - Writing assistance
- **obsidian-git** - Git integration for version control
- **obsidian-icon-folder** - Custom folder icons

### Git Auto-backup Settings
- Auto-commit every 5 minutes with message: "vault backup: YYYY-MM-DD HH:mm:ss"
- Auto-push every 5 minutes
- Auto-pull every 5 minutes on boot
- Pull before push enabled

## Working with This Vault

### Essential Commands and Operations

#### Git Operations (Automated)
The vault uses the obsidian-git plugin with automated backup:
- **Auto-commit**: Every 5 minutes with message format "vault backup: YYYY-MM-DD HH:mm:ss"  
- **Auto-push/pull**: Every 5 minutes
- **Manual git operations**: Available through Obsidian Command Palette (Ctrl/Cmd+P)

#### Content Management Commands
- Use Obsidian's built-in search (Ctrl/Cmd+Shift+F) or omnisearch plugin for enhanced search
- Dataview plugin enables database-like queries using `dataview` code blocks
- Templater plugin provides advanced template functionality with 4 active templates

### File Naming Conventions
- Daily notes: `YYYY-MM-DD.md`
- Books: `Author-Title.md` 
- Projects: Descriptive names with spaces
- Archive items: Descriptive names, organized by completion date

### Content Organization Architecture
- **PARA Method**: Projects (active with deadlines), Areas (ongoing responsibilities), Resources (future reference), Archives (inactive)
- **Export section**: Contains imported content from external systems, organized by source/person
- **Language preservation**: Japanese content maintained in original language
- **Hierarchical structure**: Folders can contain both markdown files and subfolders for detailed organization

### Note-taking Practices
- Daily reflections and progress tracking in `01_daily/`
- Book summaries with key insights in `30_resources/literature/`
- Project documentation and meeting notes in `10_projects/`
- Atomic knowledge notes in `02_zettelkasten/` with explicit linking
- Startup and business planning materials in `20_areas/business/`

## Development Context

This vault belongs to someone involved in:
- Programming education and 42Tokyo
- Startup planning and entrepreneurship
- Home tutoring business
- AI and technology learning
- Personal development and reading

The content suggests active work on business development, technical learning, and personal knowledge management.

## Technical Architecture

### Plugin Integration
This vault relies heavily on community plugins for enhanced functionality:

- **dataview**: Enables SQL-like queries for note aggregation and analysis
- **excalibrain**: Provides visual knowledge graph representation  
- **obsidian-excalidraw-plugin**: Integrated drawing and diagramming
- **templater-obsidian**: Advanced templating system with 4 active templates
- **omnisearch**: Enhanced full-text search capabilities
- **obsidian-git**: Automated version control and backup system
- **typing-assistant**: Writing assistance and productivity features
- **recent-files-obsidian**: Quick access to recently modified files
- **obsidian-icon-folder**: Visual folder customization

### Backup and Version Control Strategy
- **Automated commits**: Every 5 minutes via obsidian-git plugin
- **Remote synchronization**: Auto-push/pull every 5 minutes  
- **Conflict resolution**: Pull-before-push enabled to prevent conflicts
- **Branch strategy**: Works on main branch with automatic backup commits

### Important Notes for Development
- This is a **personal knowledge management system**, not a software project
- No build processes, test suites, or deployment pipelines exist
- The "codebase" consists entirely of markdown files and Obsidian configuration
- All automation is handled through Obsidian plugins, not external scripts
- Content is primarily in markdown format with some CSV exports from external systems

## Vault Maintenance Tools

The `99_meta/` directory contains organized maintenance tools:

```
99_meta/
├── scripts/          # Maintenance scripts
├── docs/            # Documentation and reports
└── logs/            # Log files
    └── archive/     # Archived logs
```

### Cleanup Operations
- **`scripts/cleanup_uuid_files.py`** - Original UUID cleanup script (legacy)
  - Basic UUID pattern removal and link updates
  
- **`scripts/enhanced_uuid_cleanup.py`** - Advanced UUID cleanup with improved pattern matching
  - Usage: `python3 99_meta/scripts/enhanced_uuid_cleanup.py`
  - Handles space-prefixed UUID patterns and 32-character hex suffixes
  - Automatically updates markdown internal links after renaming
  - Successfully processed 1,695 files and renamed 76 during optimization

- **`scripts/check_broken_links.py`** - Identifies broken internal links in the vault
  - Usage: `python3 99_meta/scripts/check_broken_links.py`
  - Scans all markdown files for `[[link]]` and `[text](link.md)` patterns
  - Generates detailed report of broken links by file
  - Essential for maintaining link integrity after file reorganization

- **`scripts/fix_broken_links.py`** - Repairs common broken link patterns
  - Usage: `python3 99_meta/scripts/fix_broken_links.py`
  - Fixes template placeholders, URL-encoded links, and generic broken patterns
  - Successfully repaired 29 files during vault optimization

- **`scripts/zettelkasten_optimization.sh`** - Comprehensive vault optimization script
  - Usage: `./99_meta/scripts/zettelkasten_optimization.sh [backup|cleanup|consolidate|frontmatter|validate|all]`
  - Supports dry-run mode (default): `DRY_RUN=true ./99_meta/scripts/zettelkasten_optimization.sh all`
  - Execute mode: `DRY_RUN=false ./99_meta/scripts/zettelkasten_optimization.sh all`
  - Phases: backup, cleanup empty files, consolidate IDEA FLASH GLOBAL, add frontmatter, validate links
  - Automatically creates git branches and commits for safe operations

### Maintenance Commands
When working with the vault structure:
1. **Comprehensive optimization**: `./99_meta/scripts/zettelkasten_optimization.sh all` (dry-run by default)
2. **Link integrity check**: `python3 99_meta/scripts/check_broken_links.py`
3. **UUID cleanup (advanced)**: `python3 99_meta/scripts/enhanced_uuid_cleanup.py`
4. **Broken link repair**: `python3 99_meta/scripts/fix_broken_links.py`
5. **Git status check**: Standard git commands work due to obsidian-git integration

### Optimization History
- **2025-08-11**: Complete vault optimization performed
  - UUID cleanup: 76 files renamed from 1,695 processed
  - Link repair: 29 files fixed for template placeholders and encoding issues
  - Structure consolidation: Export folders archived, duplicates removed
  - Template system: 4 comprehensive templates implemented

## Content Architecture

### Zettelkasten Implementation
- `02_zettelkasten/` contains atomic notes with explicit connection mapping
- Subdirectories: `concepts/`, `connections/`, `insights/`
- Focus on linking ideas rather than hierarchical organization

### PARA Method Structure
- **Projects (10_projects/)**: Time-bound outcomes with deadlines
- **Areas (20_areas/)**: Ongoing standards to maintain
- **Resources (30_resources/)**: Topics of ongoing interest
- **Archives (90_archive/)**: Inactive items from the above categories

### Archive Management
- Historical imports archived in `90_archive/ingested_exports_20250811/`
- Duplicate content archived in `90_archive/duplicates_20250811/`
- CSV files contain structured data from external tools
- Japanese content maintained in original language for cultural context

### Template System
The vault includes 4 comprehensive templates in `30_resources/templates/`:
- **Daily Note Template**: Daily planning with Dataview queries for task tracking
- **Project Template**: Comprehensive project management with phases and retrospectives
- **Literature Note Template**: Book/article reviews with insights and connections
- **Zettelkasten Note Template**: Atomic note structure with explicit concept linking