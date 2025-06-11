# Understanding the `.gitignore` File

## What and why?

The `.gitignore` file tells Git which files and
folders to ignore when tracking changes. Think of it as keeping the party clean by
not letting in the uninvited guests (like temporary files, build artifacts, and
system-specific files).

Our template comes with two `.gitignore` files:

1. root: `TEMPLATE/.gitignore`

    crafted to work with both Python and R development workflows. It's organized into
    logical sections to make it easy to understand and maintain.

2. data: `TEMPLATE/data/.gitignore`
    specifically designed to ignore files in the `data` directory
    pre-configured to ignore everything except the `README.md` files,
    to prevent users from accidentally rawdata files.

!!! question "Why shouldn't I commit my data files?"

    ??? Answer
        - **Large files bloat the repo:** Every clone/download pulls the whole
        history, so a single 500 MB dataset balloons to gigabytes after a few
        updates.

        - **Git is text‑oriented:** Binary data can’t be delta‑compressed well, so
        each revision is stored almost in full, slowing every operation.

        - **Privacy!:** Patient or proprietary data in a public repo is dangerous
        and can lead to Data Use Agreements being violated.

        - **Reproducibility best practice:** Keep code in Git and store immutable
        data elsewhere (e.g. Zenodo, FigShare) so others can fetch the exact
        snapshot you used AND use it across different projects.

        - **Backup strategy separation:** Repos are for source; archives belong in
        object storage, not in version control.

        - **CI/CD efficiency:** Smaller repositories mean faster pipelines and lower
        bandwidth costs for every contributor.

## What's inside the main `.gitignore` file?

The `.gitignore` file is organized into these major sections:

1. **Operating System files** - Keeps those pesky `.DS_Store` files (macOS),
   Thumbs.db (Windows), and other OS-specific clutter out of your repository
2. **Python related files** - Ignores bytecode, package builds, and other
   Python-specific temporary files
3. **R related files** - Skips R history, session data, and package build files
4. **IDE/Editor files** - Prevents editor configs from PyCharm, VS Code, and
   others from being shared
5. **Dependency Management** - Handles ignoring appropriate files from tools like
   poetry, pipenv, and pdm
6. **Build/Test artifacts** - Keeps build directories and test results from
   cluttering your repo
7. **Documentation builds** - Ignores generated documentation that should be built
   on-demand
8. **Project-specific entries** - A section reserved for your specific project needs

## Why is this important?

A well-configured `.gitignore` file:

- **Keeps your repository clean** - No more accidental commits of temporary files
- **Reduces conflicts** - Prevents system-specific files from causing merge headaches
- **Improves performance** - Git works faster when it doesn't have to track
  thousands of irrelevant files
- **Maintains security** - Prevents accidental commits of sensitive information
  (like environment files)

!!! tip
    If you find yourself repeatedly using `git add -f` to force-add ignored files,
    that might be a sign you need to adjust your `.gitignore` file.

!!! warning "Handle with care"
    The `.gitignore` file in this template has been carefully optimized for data
    science projects using Python and R. **Modify it only if you know what you're
    doing!**

    Removing patterns can lead to system files, caches, or even sensitive information
    being accidentally committed to your repository.

## Customizing for your project

Need to add project-specific patterns? Look for the "PROJECT-SPECIFIC ENTRIES"
section at the end of the file:

    #############################################################################
    # 8. PROJECT-SPECIFIC ENTRIES
    #############################################################################
    
    # Add your project-specific entries here
    # For example:
    # models/
    # sandbox/
    # etc.

This is where you can safely add patterns specific to your project without
disrupting the carefully balanced patterns above.

!!! example "Common additions"
    You might want to add patterns for:

    - Large data files (`sandbox/` directory if you use it)
    - Model checkpoints or weights (`.h5`, `.pkl`)
    - Generated figures or outputs
    - Environment-specific configuration files (`.env`, `.local`)
    - Temporary directories (`temp/`, `cache/`)
