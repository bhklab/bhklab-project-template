import logging
from pathlib import Path

from damply import dirs

logging.basicConfig(
	level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main() -> None:
	print(f'{dirs.PROJECT_ROOT=}')

	print(f'{dirs.RAWDATA=} has {len(list(dirs.RAWDATA.glob("*")))} files')
	print(f'{dirs.PROCDATA=} has {len(list(dirs.PROCDATA.glob("*")))} files')
	print(f'{dirs.SCRIPTS=} has {len(list(dirs.SCRIPTS.glob("*")))} files')

	# these are all available via the `dirs`` object
	# CONFIG       : ├── config
	# LOGS         : ├── logs
	# METADATA     : ├── metadata
	# NOTEBOOKS    : ├── workflow/notebooks
	# PROCDATA     : ├── data/procdata
	# RAWDATA      : ├── data/rawdata
	# RESULTS      : ├── data/results
	# SCRIPTS      : └── workflow/scripts


if __name__ == '__main__':
	logger.info(f'Starting example script from {Path().cwd()=}')
	main()
