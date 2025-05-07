# Project Template for BHKLab Projects

## Usage

**Step 1: Make sure you have the `pixi` tool installed.**

Visit the [pixi documentation](https://pixi.sh)

**Step 2: Run the following command to create a new project.**
**Replace `${PROJECT_NAME}` with the name of your project.**

```console
pixi exec --spec copier -- copier copy --trust --vcs-ref HEAD https://github.com/bhklab/bhklab-project-template <PROJECT_NAME>
```

## How this works

This project uses the [copier tool](https://copier.readthedocs.io) to maintain
a standardized project template that follows the general structure of BHKLab
repositories.

Copier facilitates the management of project templates by
using [jinja2](https://jinja.palletsprojects.com/) templating for file/directory
names and content in the template.

## Setting up GitHub Actions

**Step 1: Go to `settings` > `Actions` > `General` in your GitHub repository.**
![actions-general](./assets/actions-general-settings.png)

**Step 2: Select `Allow all actions and reusable workflows` in the `Workflow permissions` section + CLICK `Save`**
![actions-permissions](./assets/actions-permissions-settings.png)

**Step 3: Scroll down to the `Workflow permissions` section and select `Read and write permissions AND Allow GitHub Actions to create and approve pull requests`**
![actions-permissions](./assets/actions-permissions-settings-2.png)

## Issues

Please report any issues with the template to the
[bhklab/bhklab-project-template](https://github.com/bhklab/bhklab-project-template).
