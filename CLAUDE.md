# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Obsidian personal knowledge vault** organized using the PARA method (Projects, Areas, Resources, Archives). The vault contains personal notes, literature summaries, daily logs, and project documentation in markdown format.

## Repository Structure

- `00_inbox/` - Temporary notes and unprocessed content
- `10_daily/` - Daily notes and logs (format: YYYY-MM-DD.md)
- `20_literature/` - Book summaries and research notes
  - `20_literature/kindle/` - Kindle book highlights and summaries
  - `20_literature/meetings/` - Meeting notes and documentation
- `30_ideas/` - Ideas and creative content (currently empty)
- `40_projects/` - Active project files (currently empty)
- `80_scripts/` - Automation scripts (currently empty)
- `90_assets/` - Media files and resources (currently empty)
- `99_archive/` - Completed or inactive content
- `Export-f05c4e37-482b-4c13-92b8-97b944be36c2/` - Exported content from external systems
- `templates/` - Note templates
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
- Templater plugin provides advanced template functionality (no templates currently configured)

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
- Daily reflections and progress tracking in `10_daily/`
- Book summaries with key insights in `20_literature/kindle/`
- Project documentation and meeting notes under respective folders
- Startup and business planning materials in personal sections

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
- **templater-obsidian**: Advanced templating system (currently no templates configured)
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