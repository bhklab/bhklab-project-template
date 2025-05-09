# Project Template for BHKLab Projects

[![Test Copier Template](https://github.com/bhklab/bhklab-project-template/actions/workflows/test-template.yml/badge.svg)](https://github.com/bhklab/bhklab-project-template/actions/workflows/test-template.yml)
[![Validate Copier Template](https://github.com/bhklab/bhklab-project-template/actions/workflows/validate-template.yml/badge.svg)](https://github.com/bhklab/bhklab-project-template/actions/workflows/validate-template.yml)

## How this works

This project uses the [copier tool](https://copier.readthedocs.io) to maintain
a standardized project template that follows the general structure of BHKLab
repositories.

Copier facilitates the management of project templates by
using [jinja2](https://jinja.palletsprojects.com/) templating for file/directory
names and content in the template.

## Template Testing

This template includes GitHub Actions that automatically test and validate the template:

### Test Copier Template Workflow
This action tests the template on multiple operating systems (Ubuntu, macOS, and Windows) to ensure it can be built with copier. The action performs the following steps:

1. Checks out the template repository
2. Sets up pixi
3. Installs dependencies
4. Creates a test project using copier (non-interactive mode)
5. Validates the generated project structure and files
6. Tests the pixi environment in the generated project

### Validate Copier Template Workflow
This action validates the template structure and syntax:

1. Checks for required files and directories
2. Validates YAML syntax in configuration files
3. Checks Jinja template syntax for errors

You can view the status of these tests in the GitHub Actions tab or run them manually using the workflow_dispatch event.

## Project Status and Roadmap

> [!NOTE]
> This section tracks the development progress of the BHKLab project template.

### Project Overview

The BHKLab project template aims to provide:

- Simple project setup with pixi, mkdocs, and basic DMP folder structure
- Support for reproducible research with proper documentation
- GitHub integrations and standardized workflow

### Implementation Status

- [x] Basic template structure with copier
- [x] Pixi integration with conda-forge/bioconda channels and platforms (linux-64, osx-arm64, win-64, osx-64)
- [x] DMP structure with proper README files
  - [x] workflow/notebooks
  - [x] workflow/scripts
  - [x] data/rawdata (gitignored with README)
  - [x] data/procdata (gitignored with README)
  - [x] data/results (gitignored with README)
- [x] MkDocs setup with basic pages structure
  - [x] Home page (links to README)
  - [x] Usage page (how to run code)
  - [x] Data Sources page (documentation for rawdata)
  - [x] Developer Notes page (working notes/journal)
- [x] GitHub repository creation automation with gh CLI
- [x] GitHub Pages setup with automatic deployment
- [x] GitHub Actions workflow for releases
- [ ] Example walkthrough of creating a project with the template
- [ ] Add pre-commit hooks for basic quality checks
- [ ] GitHub Actions to audit DMP structure (check for accidental commits in data directories)
- [x] Conventional PR title enforcement in GitHub Actions
- [ ] Add section for future links to manuscript/publication in README template
- [ ] Create additional environment for snakemake workflows if needed
- [ ] Add optional R project template support
- [ ] Create testing framework for the template itself

### Latest Meeting Notes (Apr 25, 2025)

<details>
<summary>Meeting Agenda and Action Items</summary>

**Template Ideas:**

- Simple/Project structure with pixi, mkdocs, basic DMP folder setup
- Package development templates for R and Python with project toml, ruff, CodeRabbit, Code coverage

**MkDocs Components:**

- Home
- How to run code
- Where to get data
- Working notes
- Documenting symbolic links

**GitHub Actions:**

- Check for presence of rawdata, procdata, results directories
- Documentation audits
- Optional CodeRabbit integration

**Action Items:**

- Complete initial template structure ✓
- Document DMP best practices ✓
- Setup GitHub Actions workflows 🚧
- Test with real projects 🚧

</details>

## Requirements

**1: Make sure you have the `pixi` tool installed.**

Visit the [pixi documentation](https://pixi.sh)

The following two commands should work:

```console
pixi exec gh --help
```

```console
pixi exec copier --help
```

**2: Make sure you have the `gh` github cli tool installed and logged in**

```console
pixi exec gh --version
```

```console
pixi exec gh auth login --hostname 'github.com' --git-protocol https
```

Follow the instructions to authenticate with your GitHub account.

> [!WARNING]
> Make sure you have been added to our lab organization(s) before proceeding!

## Usage

**Run the following command to create a new project.**
**Replace `${PROJECT_NAME}` with the name of your project.**

```console
pixi exec copier copy --trust --vcs-ref HEAD https://github.com/bhklab/bhklab-project-template <PROJECT_NAME>
```

## Troubleshooting

I have tried to simplify this setup as much as possible including the setup
of the remote GitHub repository and the GitHub Actions workflow, and deploying
the documentation to GitHub Pages.
However in case you run into issues, here are some troubleshooting steps.

<details>
<summary>extra setup steps if needed</summary>

## Setting up GitHub Actions

**Step 1: Go to `settings` > `Actions` > `General` in your GitHub repository.**
![actions-general](./assets/actions-general-settings.png)

**Step 2: Select `Allow all actions and reusable workflows` in the `Workflow permissions` section + CLICK `Save`**
![actions-permissions](./assets/actions-permissions-settings.png)

**Step 3: Scroll down to the `Workflow permissions` section and select `Read and write permissions AND Allow GitHub Actions to create and approve pull requests`**
![actions-permissions](./assets/actions-permissions-settings-2.png)

## Setting up GitHub Pages

>[!NOTE]
> Before being able to deploy the documentation, you need to set up GitHub Pages.
> This is a one-time setup for the repository. The documentation will be deployed
> automatically to GitHub Pages when you push to the `main` branch.
> However, you need to create a `gh-pages` branch in your repository.
> You can do this by running the following command:
    ```console
    git branch gh-pages
    git push origin gh-pages
    ```
> This is only possible after you have created the repository on GitHub.

The template will use mkdocs to build the documentation and deploy it to GitHub Pages.
To set up GitHub Pages, follow these steps:
**Step 1: Go to `settings` > `Pages` in your GitHub repository.**

**Step 2: Select `Deploy from a branch` in the `Source` section.**

**Step 3: Select `gh-pages` branch and `/ (root)` folder in the `Branch` section.**

**Step 4: Click `Save`.**
![gh-pages](./assets/gh-pages-settings.png)

</details>

## Issues

Please report any issues with the template to the
[bhklab/bhklab-project-template](https://github.com/bhklab/bhklab-project-template).

## Contributors

- Jermiah Joseph (@jjjermiah)
