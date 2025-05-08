# Notebooks Directory

## Purpose

This directory contains **Jupyter/RMarkdown/Quarto notebooks** used for:

- Interactive data exploration and visualization
- Prototype analysis development
- Results generation with embedded documentation
- Educational demonstrations of analysis methods

## Best Practices for Notebooks

To ensure your notebooks are useful to others:

- Include markdown cells that explain the purpose and methodology
- Document all data inputs and their sources
- Keep code cells focused and documented with comments
- Include visualization outputs in the committed notebook
- Consider using [nbdev](https://nbdev.fast.ai/) or similar tools for notebook-driven development

## Git Synchronization

Unlike data directories, **notebooks ARE tracked in Git** and should be:

- Well-documented with clear purposes
- Cleaned of large outputs before committing (consider tools like [nbstripout](https://github.com/kynan/nbstripout))
- Named descriptively (e.g., `01_data_exploration.ipynb`, `02_feature_selection.ipynb`)
WARNING: if the data you are working with cannot be publicly shared (e.g. internal datasets), make sure no results are pushed to Git in your notebooks!
## Organization Recommendations

Organize notebooks in a logical sequence that follows your analysis workflow:

1. Data loading and exploration notebooks
2. Data processing notebooks
3. Analysis notebooks
4. Visualization and results notebooks

## Data References

When accessing data in notebooks:

- Use relative paths with symbolic links to reference data in the `data/` directories
  - **DO NOT** hard-code absolute paths like `/home/user/project/data/rawdata/` or `/cluster/project/data/rawdata/`
- Document the specific data files used in markdown cells

Remember that notebooks serve as interactive documentation of your analysis process and should be readable and reproducible by others!
