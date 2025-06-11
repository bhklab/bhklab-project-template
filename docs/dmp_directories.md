# Working with DMP Directories

Over the years, we have developed a standardized directory structure via the
data management plan (DMP) in our projects. This structure is designed to:

- Facilitate reproducible research
- Provide a clear organization for data, code, and documentation
- Support collaboration and data sharing
- Promote familiarity and ease of use across projects

!!! danger "Understanding DMP Directories is *mandatory* in the BHKLab"

    This page is just a brief overview of the DMP directory structure.
    For a comprehensive overview, please take the time to read and
    understand the [damply documentation](
    https://bhklab.github.io/damply/).

The standardized DMP directory structure is implemented via the
[`damply`](https://github.com/bhklab/damply) package, which provides tools and
conventions for organizing project files in accordance with DMP guidelines.

!!! question "DMP reproducibility litmus test"

    If you are unsure whether your project is DMP-reproducible, ask yourself the
    following questions:

    - If I had no prior knowledge of the data used in this project,
      does the documentation provide enough information to understand
      the data, its sources, and how to obtain it?
    - If I were a new collaborator, would I be able to understand the code
      and documentation I need to understand and reproduce the project?
    - If I were to delete all the `procdata` and `results` directories,
      could I reproduce the results with just the `rawdata` and workflow content?

## DMP Directory Structure

As of writing, the recommended directory structure is as follows:

```console
project_root/
├── config/         # Configuration files
├── data/           # All data in one parent directory
│   ├── procdata/   # Processed/intermediate data
│   ├── rawdata/    # Raw input data
│   └── results/    # Analysis outputs
├── logs/           # Log files
├── metadata/       # Dataset descriptions
└── workflow/       # Code organization
    ├── notebooks/  # Jupyter notebooks
    └── scripts/    # Analysis scripts
```

### `DamplyDirs` Overview

Assuming the above directory structure, the `damply` package provides a
simple way to access these directories via the `DamplyDirs` class.

This class takes advantage of the following environment variables that are
defined in the template's `pixi.toml` file:

```toml
[activation]
# convenient variables which can be used in scripts
env.CONFIG = "${PIXI_PROJECT_ROOT}/config"
env.METADATA = "${PIXI_PROJECT_ROOT}/metadata"
env.LOGS = "${PIXI_PROJECT_ROOT}/logs"
env.RAWDATA = "${PIXI_PROJECT_ROOT}/data/rawdata"
env.PROCDATA = "${PIXI_PROJECT_ROOT}/data/procdata"
env.RESULTS = "${PIXI_PROJECT_ROOT}/data/results"
env.SCRIPTS = "${PIXI_PROJECT_ROOT}/workflow/scripts"
```

This allows you to programmatically access the directories in your project
without hardcoding paths, making your code more portable and easier to
maintain.

### Example Usage

Here is an example of how to use the `DamplyDirs` class in your project:

```python
from damply import dirs

fastq_file = dirs.RAWDATA / "fastq" / "sample_1.fq.gz"
print(f"Processing FASTQ file: {fastq_file}")
# Processing FASTQ file: /home/bhkuser/proejcts/data/rawdata/fastq/sample_1.fq.gz
```

A full comprehensive walkthrough of the `DamplyDirs` utility can be found in the
[damply documentation](https://bhklab.github.io/damply/dmpdirs/).
