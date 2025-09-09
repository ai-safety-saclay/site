# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a static website generator for the PIAF association (piaf-saclay.org), built in Python using Jinja2 templating, Markdown processing, and SCSS compilation. The site features Bootstrap styling and generates HTML pages from templates and markdown content.

## Dependencies and Environment

- Uses `uv` for Python dependency management (as per user preference)
- Python 3.13+ required
- Key dependencies: Jinja2, Markdown, libsass, GitPython, Bootstrap

## Common Development Commands

### Environment Setup
```bash
# Create and activate virtual environment (use uv when possible)
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install .
```

### Build and Development
```bash
# Build the entire site
python3 __main__.py

# Start local development server after building
cd ./build
python3 -m http.server 8080

# Site will be available at http://localhost:8080
```

### Content Development
```bash
# Add new blog post - create .md file in blog/ directory
# Add new page - create template in pages/ directory
# Modify styles - edit scss/style.scss (auto-compiled during build)
```

## Architecture Overview

### Core Build System (`__main__.py`)
- **Static site generator**: Single Python script orchestrates the entire build process
- **Template engine**: Uses Jinja2 with custom extensions for Markdown processing
- **Asset pipeline**: Compiles SCSS, downloads Bootstrap/Popper.js, copies static assets
- **Content processing**: Converts Markdown files to HTML with YAML frontmatter support

### Directory Structure
```
├── __main__.py           # Main build script and site generator
├── pages/               # Jinja2 HTML templates for main pages
├── components/          # Reusable Jinja2 template components
├── blog/                # Markdown blog posts with YAML metadata
├── scss/                # SCSS stylesheets (compiled to build/style.css)
├── static/              # Static assets (images, etc.)
├── build/               # Generated site output (created during build)
├── *.yml                # Event data files (asimov.yml, lectures.yml, jeudia.yml)
```

### Template System
- **Base template**: `components/base.html` provides common HTML structure
- **Page templates**: In `pages/` directory, extend base template with specific content
- **Components**: Reusable elements in `components/` (navbar, footer, cards, etc.)
- **Template inheritance**: Uses Jinja2's `extends` and `include` for modularity

### Content Management
- **Blog posts**: Markdown files in `blog/` with YAML frontmatter for metadata
- **Event data**: YAML files (`asimov.yml`, `lectures.yml`, `jeudia.yml`) for event listings
- **Page content**: Mix of Jinja2 templates and Markdown files in `pages/`

### Build Process
1. **Cleanup**: Removes existing `build/` directory
2. **Dependencies**: Clones Bootstrap and Bootstrap Icons if not present
3. **Asset copying**: Copies static files and blog documents to build directory
4. **SCSS compilation**: Compiles `scss/style.scss` to `build/style.css`
5. **External assets**: Downloads Popper.js and copies Bootstrap JavaScript
6. **Page generation**: Processes all templates and generates HTML files
7. **Content processing**: Converts blog posts and markdown pages to HTML

### Configuration Constants
- Global site constants defined in `__main__.py`: URLs, keywords, description
- Markdown extensions: Math support, code fencing, tables, wikilinks, admonitions
- Bootstrap integration: v5.3.3 with custom SCSS compilation

## File Modification Patterns

### Adding New Pages
1. Create template in `pages/` directory (`.html` or `.md`)
2. Add `generate_page()` call in `__main__.py` if needed
3. Update navigation in `components/navbar.html` if required

### Modifying Styles
- Edit `scss/style.scss` - automatically compiled during build
- Bootstrap variables can be overridden in SCSS

### Adding Blog Posts
- Create `.md` file in `blog/` directory with YAML frontmatter
- Include `title` in frontmatter - automatically processed during build

### Updating Events
- Modify corresponding YAML file (`asimov.yml`, `lectures.yml`, `jeudia.yml`)
- Events marked with `past: true/false` are automatically sorted

## External Dependencies
- **Bootstrap**: Auto-downloaded from GitHub (v5.3.3)
- **Bootstrap Icons**: Auto-downloaded from GitHub (v1.11.3)
- **Popper.js**: Downloaded from CDN during build
- **MathJax**: Loaded from CDN for mathematical expressions
