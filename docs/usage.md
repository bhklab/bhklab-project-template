# Usage

**Run the following command to create a new project.**
**Replace `<PROJECT_NAME>` with the name of your project.**

## using `pixi`

```console
pixi exec bhklab-project-template <PROJECT_NAME>
```

- i.e `gdcs-drug-combo` would create a directory called `gdcs-drug-combo`

```console
pixi exec bhklab-project-template gdcs-drug-combo
```

## using `uv`

```console
uvx bhklab_project_template <PROJECT_NAME>
```

## using `copier`

```console
copier copy --trust gh:bhklab/bhklab-project-template <PROJECT_NAME>
```

- This will create a new directory with the name of your project and copy the
  template files into it.
