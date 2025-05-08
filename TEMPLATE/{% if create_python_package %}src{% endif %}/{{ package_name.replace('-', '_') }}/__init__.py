import logging
import random
import string

# Configure basic logging
logging.basicConfig(
	level=logging.WARNING,
	format='%(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)


def generate_random_string(length: int = 5) -> str:
	"""
	Generate a random string of specified length.

	Args:
	    length: The length of the string to generate (default: 5)

	Returns:
	    A randomly generated string
	"""
	logger.debug(f'Generating random string of length {length}')

	chars = string.ascii_lowercase
	result = ''.join(random.choice(chars) for _ in range(length))
	return result


def is_even_number(number: int) -> bool:
	"""
	Check if a number is even.

	Args:
	    number: The number to check

	Returns:
	    True if the number is even, False otherwise
	"""
	return number % 2 == 0
