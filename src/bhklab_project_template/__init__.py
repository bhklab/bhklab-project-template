"""BHKLab Project Template.

A Python package that creates new BHKLab projects from a template.
"""

__version__ = "0.11.0"

from pathlib import Path

import copier
import rich_click as click

from bhklab_project_template.logging_config import configure_logging, logger
from bhklab_project_template.utils import check_all_requirements

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
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug logging.",
)
@click.help_option(
    "-h",
    "--help",
    help="Show this message and exit.",
)
def cli(
    destination: Path,
    debug: bool = False,
) -> None:
    """Create a new BHKLab project from a template.

    DESTINATION is the path to the new project directory.
    """
    # Configure logging based on debug flag
    configure_logging(debug=debug)

    # debug log that a new project is being created
    logger.debug(f"Creating new project at {destination}")

    # Check all requirements before running the template
    check_all_requirements()

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
