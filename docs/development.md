# Development & Contribution Guide

This project uses the [copier tool](https://copier.readthedocs.io). If you want
to contribute to the project template, please take the time to read the copier
documentation on how projects are configured and how to use it.

## How projects are created from templates

For the `bhklab-project-template`, the project is created not by using
the `copier` command directly, but rather via the the python API that is
exposed by the `copier` package. This is done to allow for more flexibility
and customization of the project creation process.

You can find the code that creates the project in the
[`src/bhklab_project_template/__init__.py`](https://github.com/bhklab/bhklab-project-template/blob/main/src/bhklab_project_template/__init__.py). We wrap the API in a [`click`](https://click.palletsprojects.com/en/stable/)
command line interface.

I chose this route to make it ***super simple*** to get started and to remove
the friction in the experience of creating a new project.

## Contributing to the project template

The project template is made up of the following:

1. the [`copier.yml`](https://github.com/bhklab/bhklab-project-template/blob/main/copier.yml)
  which defines the questions to ask when creating a new project, and saves
  the answers to be used by `copier` to fill in the template files.
2. the [`TEMPLATE`](https://github.com/bhklab/bhklab-project-template/tree/main/TEMPLATE)
    directory which contains the files that will be copied to the new project.
    The files in this directory are templated using the
    [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) templating engine
    and the answers provided in the `copier.yml` file.
3. the [`src/bhklab_project_template`](https://github.com/bhklab/bhklab-project-template/tree/main/src/bhklab_project_template) directory which contains the code that implements the project template.
4. the [`copier-settings.yml`](https://github.com/bhklab/bhklab-project-template/blob/main/copier-settings.yml)
    which is just an extension of the `copier.yml` file via the [`include` feature](https://copier.readthedocs.io/en/stable/configuring/#include-other-yaml-files) of `copier`.
    This file defines some constant variables used in the workflow, and more
    importantly, it defines the [`copier` tasks](https://copier.readthedocs.io/en/stable/configuring/#tasks)
    that are run after the project is created.

## Contributing `damply` and the `DamplyDirs` utility

The `DamplyDirs` utility is provided via the `damply` package, and is already
included in the [project template's `pixi.toml` file](https://github.com/bhklab/bhklab-project-template/blob/main/TEMPLATE/pixi.toml.jinja)

If there are any issues or features that you would like to see in the
`damply` package, please open an issue or a pull request in the
[`bhklab/damply` repository](https://github.com/bhklab/damply)

