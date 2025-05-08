# Scripts Directory

## Purpose

This directory contains **reusable code scripts** for:

- Data processing pipelines
- Analysis workflows
- Utility functions
- Automation tasks

## Best Practices for Scripts

For maximum usability, scripts should:

- Include a detailed docstring/header explaining purpose, inputs, outputs
- Contain inline comments for complex logic
- Be modular and follow the single responsibility principle
- Include proper error handling and logging
- Have command-line interfaces when appropriate

## Git Synchronization

Scripts **ARE tracked in Git** and represent the core reproducible components of your analysis. Ensure scripts:

- Are well-tested before committing
- Have clear versioning (consider semantic versioning)
- Include usage examples in comments or separate documentation

## Organization Recommendations

Consider organizing scripts by their function:

```console
/scripts/preprocessing/
/scripts/analysis/
/scripts/visualization/
/scripts/utilities/
```

## Data References

When scripts access data:

- Use command-line arguments or configuration files for file paths
- Document in `docs/data_sources.md` which scripts use which data sources
- Consider using symbolic links for consistent references across environments

## Documentation Requirement

It is **highly recommended** to convert scripts to CLI tools using popular libraries
like `click` or `typer`, which can make them more user-friendly and easier to document.

```console
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Usage: script_name.py [options] <input> <output>

Arguments:
    input     Description of input
    output    Description of output

Options:
    -h --help     Show this help
    -v --verbose  Verbose output
"""
```

Remember that well-documented scripts are essential for reproducible research and enable others to understand and build upon your work!
