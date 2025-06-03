"""
A configured logger using the loguru library.
"""

import sys
from pathlib import Path

from loguru import logger
from platformdirs import user_log_dir

APP_NAME = "bhklab_project_template"
APP_AUTHOR = "bhklab"


def configure_logging(debug: bool = False) -> None:
    """
    Configures the logging settings for the application.

    Args:
        debug: If True, sets the stderr logger level to DEBUG instead of INFO.
    """
    from bhklab_project_template import __version__ as version

    logger.remove()  # Remove default logger
    logger.add(
        sys.stderr,
        level="DEBUG" if debug else "INFO",
        format="<green>{time}</green> <level>{level}</level> <cyan>{message}</cyan>",
        colorize=True,
    )

    log_dir = Path(
        user_log_dir(
            appname=APP_NAME, appauthor=APP_AUTHOR, version=version, ensure_exists=True
        )
    )
    logger.debug(f"Log directory: {log_dir}")
    logger.add(
        log_dir / f"{APP_NAME}.log",
        level="DEBUG",
        rotation="10 MB",  # Rotate log files when they reach 10 MB
        retention="30 days",  # Keep logs for 30 days
        backtrace=True,  # Include backtrace in logs
        diagnose=True,  # Include diagnostic information
        enqueue=True,  # Use a queue for logging to avoid blocking
        catch=True,  # Catch exceptions and log them
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    )
    logger.bind(name=APP_NAME)
