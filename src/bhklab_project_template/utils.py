import subprocess
from typing import Optional

from bhklab_project_template.logging_config import configure_logging, logger

# Central constants for version requirements
REQUIREMENTS_URL = "https://bhklab.github.io/bhklab-project-template/requirements/"
MIN_GIT_VERSION = (2, 28)
MIN_PIXI_VERSION = (0, 47, 0)

# Configure logging when this module is imported
configure_logging()


def check_git_version() -> None:
    """
    Our copier template requires git >= 2.28.

    This is because we use the `--initial-branch` option in the
    `git init` command, and we need to make sure user's git
    version is compatible with this option.
    If the git version is too old, we raise an error with a link
    to the issue where this is discussed.

    https://github.com/bhklab/bhklab-project-template/issues/30
    """
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        version_str = result.stdout.strip().split()[-1]
        major, minor, _ = map(int, version_str.split("."))
        logger.debug(f"Git version: {version_str}")
        if (major, minor) < MIN_GIT_VERSION:
            logger.error(
                f"Your git version {version_str} is too old (requires >= {MIN_GIT_VERSION[0]}.{MIN_GIT_VERSION[1]})"
            )
            raise RuntimeError(
                "Your git version is too old. "
                f"Detected version: {version_str}. "
                f"Please update to git >= {MIN_GIT_VERSION[0]}.{MIN_GIT_VERSION[1]}. "
                f"See {REQUIREMENTS_URL} for more information."
            )
    except subprocess.CalledProcessError:
        logger.error("Failed to determine git version")
        raise RuntimeError(
            "Could not determine git version. "
            "Please make sure git is installed and accessible. "
            f"See {REQUIREMENTS_URL} for more information."
        )


def check_pixi_installation() -> None:
    """
    Verifies that pixi is installed and accessible.

    Our project template uses pixi for environment management and to execute
    commands through GitHub CLI (gh). This function checks if pixi is properly
    installed and has minimum version 0.47.0.
    """
    try:
        result = subprocess.run(
            ["pixi", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        version_str = result.stdout.strip().split()[-1]
        # Parse version string to compare with minimum version
        version_parts = tuple(map(int, version_str.split(".")))

        logger.debug(f"Pixi version: {version_str}")

        if version_parts < MIN_PIXI_VERSION:
            min_version_str = ".".join(map(str, MIN_PIXI_VERSION))
            logger.error(
                f"Pixi version {version_str} is too old (requires >= {min_version_str})"
            )
            raise RuntimeError(
                f"Your pixi version {version_str} is too old. "
                f"Please upgrade to version {min_version_str} or higher. "
                "You can do this by running 'pixi self-update'. "
                f"See {REQUIREMENTS_URL} for more information."
            )
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("Pixi installation not found")
        raise RuntimeError(
            "Pixi is not installed or not accessible. "
            "Please install pixi following the instructions at https://pixi.sh. "
            f"See {REQUIREMENTS_URL} for more information."
        )


def check_gh_login() -> Optional[str]:
    """
    Checks if the user is logged into GitHub CLI.

    Our project template requires GitHub CLI authentication for various operations
    like creating repositories. This function verifies if the user is properly
    authenticated with GitHub.

    Returns:
        Optional[str]: The GitHub username if logged in, None otherwise.
    """
    try:
        # Check if gh is accessible through pixi
        subprocess.run(
            ["pixi", "exec", "gh", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )

        # Check if user is authenticated
        result = subprocess.run(
            ["pixi", "exec", "gh", "auth", "status"],
            capture_output=True,
            text=True,
            check=False,  # Don't raise an exception if not logged in
        )

        if result.returncode != 0:
            logger.warning("User not authenticated with GitHub CLI")
            raise RuntimeError(
                "You are not logged in to GitHub CLI. "
                "Please run 'pixi exec gh auth login --hostname 'github.com' --git-protocol https' "
                "and follow the instructions to authenticate. "
                f"See {REQUIREMENTS_URL} for more information."
            )
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("GitHub CLI not accessible through pixi")
        raise RuntimeError(
            "GitHub CLI (gh) is not accessible through pixi. "
            "Please make sure pixi is installed and gh is available in the pixi environment. "
            f"See {REQUIREMENTS_URL} for more information."
        )
    else:
        logger.debug("GitHub CLI is accessible through pixi and user is authenticated")
        # Extract username from output
        for line in result.stdout.strip().split("\n"):
            if "Logged in to github.com as" in line:
                return line.split("as")[1].strip()
        return None


def check_all_requirements() -> None:
    """
    Checks all system requirements for using BHKLab Project Template.

    This function runs all necessary checks to ensure the user's system meets the
    requirements for using the project template. It verifies:
    1. Git version is 2.28 or higher
    2. Pixi is installed and accessible
    3. GitHub CLI is accessible through pixi and authenticated

    Raises:
        RuntimeError: If any requirement is not met, with a helpful message
                     directing to the documentation.
    """
    logger.info("Checking system requirements...")
    check_git_version()
    check_pixi_installation()
    username = check_gh_login()
    if username:
        logger.debug(f"All requirements met! Authenticated to GitHub as: {username}")
    else:
        logger.debug(
            "All requirements met! GitHub authentication verified but username not detected."
        )
    logger.info("You're ready to use BHKLab Project Template!")


if __name__ == "__main__":
    try:
        check_all_requirements()
    except RuntimeError as e:
        logger.error(f"System requirements check failed: {e}")
        raise
