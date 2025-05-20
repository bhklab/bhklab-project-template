"""BHKLab Project Template.

A Python package that creates new BHKLab projects from a template.
"""

__version__ = "0.10.0"

from pathlib import Path

import copier

import rich_click as click

DEFAULT_TEMPLATE = "gh:bhklab/bhklab-project-template"


@click.command()
@click.argument(
    "DESTINATION",
    required=True,
    type=click.Path(
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        resolve_path=True,
    ),
)
@click.help_option(
    "-h",
    "--help",
    help="Show this message and exit.",
)
def cli(
    destination: Path,
) -> None:
    """Create a new BHKLab project from a template.

    DESTINATION is the path to the new project directory.
    """
    copier.run_copy(
        src_path=DEFAULT_TEMPLATE,
        dst_path=destination,
        unsafe=True,
        data={
            # we could think of a way to get some default values from the user
        },
    )


if __name__ == "__main__":
    cli()
