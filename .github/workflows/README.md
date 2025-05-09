# GitHub Actions for bhklab-project-template

This directory contains GitHub Actions workflows that help maintain the quality and reliability of the bhklab-project-template.

## Workflows

### 1. Test Copier Template (`test-template.yml`)

Tests the template on multiple operating systems (Ubuntu, macOS, Windows) to ensure it can be built with copier using Pixi.

Key features:
- Multi-OS testing matrix (Ubuntu, macOS, Windows)
- Uses Pixi for environment management
- Creates a test project using non-interactive mode
- Validates the generated project structure
- Tests the Pixi environment in the generated project

### 2. Validate Copier Template (`validate-template.yml`)

Validates the template structure and syntax without actually creating a project.

Key features:
- Validates YAML syntax in configuration files
- Checks for required files and directories
- Validates Jinja template syntax

### 3. Copier Cross-Platform Compatibility (`copier-compatibility.yml`)

Tests if Copier can be run on different platforms with different Python versions without Pixi.

Key features:
- Multi-OS testing matrix (Ubuntu, macOS, Windows)
- Multiple Python versions (3.10, 3.11, 3.12)
- Uses pip to install Copier directly
- Weekly scheduled runs to catch issues with dependencies

## Manual Triggering

All workflows can be triggered manually from the GitHub Actions tab using the workflow_dispatch event.

## Status Badges

Status badges for these workflows are included in the main README.md file.
