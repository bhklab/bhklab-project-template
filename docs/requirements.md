
# Project Requirements

This document outlines the necessary prerequisites for using the BHKLab Project Template.

## System Requirements

### 1. Git Version Requirements

You must have Git version 2.28 or higher installed on your system. This is because our template uses
the `--initial-branch` option in the `git init` command.

To check your Git version:

```console
git --version
```

If your Git version is below 2.28, please update it following instructions for your operating system.

### 2. Pixi Tool Requirements

**Pixi** is our preferred package manager and environment manager for this project.

#### 2.1 Installing Pixi

If you haven't installed Pixi yet:

1. Visit the [pixi documentation](https://pixi.sh) for installation instructions
2. Follow the platform-specific instructions to install Pixi on your system

#### 2.2 Verifying Installation

After installation, run the following commands to verify that Pixi is properly installed:

```console
# Check pixi version
pixi --version

# Verify GitHub CLI is accessible through pixi
pixi exec gh --help

# Verify our project template tool is accessible
pixi exec bhklab-project-template --help
```

If any of these commands fail, please reinstall Pixi or make sure it's properly added to your PATH.

### 3. GitHub CLI Authentication

Our template interacts with GitHub APIs through the GitHub CLI tool (`gh`), which requires
authentication.

#### 3.1 Logging into GitHub CLI

Run the following command and follow the prompts to authenticate:

```console
pixi exec gh auth login --hostname 'github.com' --git-protocol https
```

#### 3.2 Verifying Authentication

To verify you're properly authenticated:

```console
pixi exec gh auth status
```

This should show that you're logged in to GitHub.

!!! warning "Organization Access"
    Make sure you have been added to our lab organization(s) before proceeding with project creation!
    Without proper organization access, you won't be able to create repositories in our shared spaces.

## Troubleshooting

If you encounter any issues setting up these requirements, please:

1. Check the error messages for specific guidance
2. Reach out to the lab's technical team if problems persist

Our project template will automatically validate these requirements and provide helpful error messages
if any prerequisites are not met.
