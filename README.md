# Project Template for BHKLab Projects

## Table of Contents

- [How this works](#how-this-works)
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Usage](#usage)
  - [using `pixi`](#using-pixi)
  - [using `uv`](#using-uv)
  - [using `copier`](#using-copier)
- [Documentation](#documentation)
  - [Meeting Notes](docs/meeting_notes.md)
  - [Status](docs/status.md)
  - [Troubleshooting](docs/troubleshooting.md)
- [Issues](#issues)
- [Contributors](#contributors)

## How this works

This project uses the [copier tool](https://copier.readthedocs.io) to maintain
a standardized project template that follows the general structure of BHKLab
repositories.

Copier facilitates the management of project templates by
using [jinja2](https://jinja.palletsprojects.com/) templating for file/directory
names and content in the template.

## Project Overview

The BHKLab project template aims to provide:

- Simple project setup with pixi, mkdocs, and basic DMP folder structure
- Support for reproducible research with proper documentation
- GitHub integrations and standardized workflow

## Requirements

**1: Make sure you have the `pixi` tool installed.**

Visit the [pixi documentation](https://pixi.sh)

The following two commands should work:

```console
pixi exec gh --help

pixi exec bhklab-project-template --help
```

**2: Make sure you have logged in to GitHub CLI.**

```console
pixi exec gh auth login --hostname 'github.com' --git-protocol https
```

Follow the instructions to authenticate with your GitHub account.

> [!WARNING]
> Make sure you have been added to our lab organization(s) before proceeding!

## Usage

**Run the following command to create a new project.**
**Replace `<PROJECT_NAME>` with the name of your project.**

### using `pixi`

```console
pixi exec bhklab-project-template <PROJECT_NAME>
```

- i.e `gdcs-drug-combo` would create a directory called `gdcs-drug-combo`

```console
pixi exec bhklab-project-template gdcs-drug-combo
```

### using `uv`

```console
uv run -m bhklab_project_template <PROJECT_NAME>
```

### using `copier`

```console
pixi exec copier copy --trust gh:bhklab/bhklab-project-template <PROJECT_NAME>
```

- This will create a new directory with the name of your project and copy the
  template files into it.

## Documentation

- [Meeting Notes](docs/meeting_notes.md)
- [Status](docs/status.md)
- [Troubleshooting](docs/troubleshooting.md)

## Issues

Please report any issues with the template to the
[bhklab/bhklab-project-template](https://github.com/bhklab/bhklab-project-template).

## Contributors

- Jermiah Joseph (@jjjermiah)
