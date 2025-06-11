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

The default approach to using the `bhklab-project-template` is to use the
`pixi exec bhklab-project-template` command, which is a neat quick
wrapper around the `bhklab-project-template`'s `CLI` entry point.
However, if you make a change to the `bhklab-project-template` package,
you need to go through some extra steps to make sure that the changes
are propagated to the users.

### 1. Make sure the changes are pushed to the `main` branch & `release-please` PR is merged

After you make changes to the project template, `release-please` will create a
pull request to update the version of the `bhklab-project-template` package.

!!! warning "Only updates pypi package version"
    The `release-please` PR will only update the version of the `bhklab-project-template`
    package in the `pyproject.toml` file, and push to `PyPi` via the
    GitHub Actions workflow.
    It will not update the version of the `bhklab-project-template` package in
    [conda-forge](https://anaconda.org/conda-forge/bhklab-project-template).

### Updating the `conda-forge` feedstock

After 1-3 hours of the `release-please` PR being merged, and the new version
being available on `PyPi`, the [`conda-forge` feedstock repo](https://github.com/conda-forge/bhklab-project-template-feedstock)
should have a PR created by the `conda-forge-bot` that updates the version
(i.e [the v0.11.0 PR](https://github.com/conda-forge/bhklab-project-template-feedstock/pull/4)).

There maintainers defined in the `recipe.yaml` file, who are responsible for
reviewing and merging the PR. If you are a maintainer, make sure all the checks
are passing, and then merge the PR. This will update the `conda-forge` feedstock
and trigger a new build of the `bhklab-project-template` package on `conda-forge`.
The version on [conda-forge](https://anaconda.org/conda-forge/bhklab-project-template)
will be updated within a few hours after the PR is merged.

**Alternatively**, you can also manually trigger a new build, by creating your own
PR and updating the **version** AND **sha256** of the `bhklab-project-template`
(see the above PR for an example). This is useful if you want to
update the `conda-forge` feedstock immediately after the `release-please` PR is merged.

## Contributing `damply` and the `DamplyDirs` utility

The `DamplyDirs` utility is provided via the `damply` package, and is already
included in the [project template's `pixi.toml` file](https://github.com/bhklab/bhklab-project-template/blob/main/TEMPLATE/pixi.toml.jinja)

If there are any issues or features that you would like to see in the
`damply` package, please open an issue or a pull request in the
[`bhklab/damply` repository](https://github.com/bhklab/damply)
