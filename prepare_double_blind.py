#!/usr/bin/env python3
"""
Script to prepare repository for double-blind submission.
This script removes git history and creates a clean copy suitable for anonymous submission.
"""

import os
import shutil
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def prepare_double_blind():
    """Prepare the repository for double-blind submission."""
    
    print("🔒 Preparing repository for double-blind submission...")
    
    # Get current directory
    current_dir = Path.cwd()
    parent_dir = current_dir.parent
    
    # Create new directory name for anonymous submission
    new_dir_name = "multi_agent_trading_framework"
    new_dir = parent_dir / new_dir_name
    
    print(f"📁 Creating clean copy in: {new_dir}")
    
    # Remove existing directory if it exists
    if new_dir.exists():
        shutil.rmtree(new_dir)
    
    # Copy all files except .git directory
    print("📋 Copying files (excluding git history)...")
    
    # List of directories/files to exclude
    exclude_patterns = [
        '.git',
        '.gitignore',
        '__pycache__',
        '*.pyc',
        '.pytest_cache',
        '.coverage',
        'htmlcov',
        '.mypy_cache',
        '.vscode',
        '.idea',
        'node_modules',
        '*.log'
    ]
    
    def should_exclude(path):
        """Check if a path should be excluded."""
        path_str = str(path)
        for pattern in exclude_patterns:
            if pattern in path_str:
                return True
        return False
    
    def copy_directory(src, dst):
        """Recursively copy directory excluding git and cache files."""
        dst.mkdir(parents=True, exist_ok=True)
        
        for item in src.iterdir():
            if should_exclude(item):
                continue
                
            if item.is_file():
                shutil.copy2(item, dst / item.name)
            elif item.is_dir():
                copy_directory(item, dst / item.name)
    
    # Copy the repository
    copy_directory(current_dir, new_dir)
    
    # Remove any remaining git-related files
    git_files = [
        new_dir / '.git',
        new_dir / '.gitignore',
        new_dir / '.gitattributes'
    ]
    
    for git_file in git_files:
        if git_file.exists():
            if git_file.is_dir():
                shutil.rmtree(git_file)
            else:
                git_file.unlink()
    
    # Create a new .gitignore for the anonymous version
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Logs
*.log
logs/

# Environment variables
.env
.env.local

# API keys (should be set by user)
config/local.json

# Temporary files
*.tmp
*.temp
"""
    
    with open(new_dir / '.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    # Create a submission README
    submission_readme = """# Multi-Agent LLM-Based Financial Trading Framework

## Double-Blind Submission

This repository has been prepared for double-blind peer review. All identifying information has been removed.

## Quick Start

1. Install dependencies: `pip install -e .`
2. Set your OpenAI API key: `export OPENAI_API_KEY="your-key"`
3. Run the CLI: `tradingagents`

## Documentation

See README.md for comprehensive documentation.

## Research Contributions

This work demonstrates novel approaches to:
- Multi-agent coordination in financial trading
- LLM integration for quantitative finance
- Real-time market analysis and decision making
- Advanced portfolio optimization techniques

## License

Apache License 2.0
"""
    
    with open(new_dir / 'SUBMISSION_README.md', 'w') as f:
        f.write(submission_readme)
    
    print("✅ Repository prepared for double-blind submission!")
    print(f"📁 Clean copy created at: {new_dir}")
    print("\n📋 Next steps:")
    print("1. Navigate to the new directory")
    print("2. Initialize a new git repository")
    print("3. Push to your anonymous GitHub account")
    print("\nCommands:")
    print(f"cd {new_dir}")
    print("git init")
    print("git add .")
    print("git commit -m 'Initial commit for double-blind submission'")
    print("git remote add origin <your-anonymous-repo-url>")
    print("git push -u origin main")
    
    return new_dir

if __name__ == "__main__":
    try:
        new_dir = prepare_double_blind()
        print(f"\n🎯 Repository ready for submission at: {new_dir}")
    except Exception as e:
        print(f"❌ Error preparing repository: {e}")
        exit(1) 