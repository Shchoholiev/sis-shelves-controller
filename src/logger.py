import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    """
    Set up and configure the logger for the shelves controller.

    Returns:
        logger: The configured logger object.
    """

    logger = logging.getLogger('shelves_controller_logger')
    logger.setLevel(logging.INFO)

    # Create a handler that writes log messages to a file, with rotation
    handler = RotatingFileHandler(
        'shelves_controller.log',  # Path to the log file
        maxBytes=15*1024*1024,  # Max log file size (15MB)
        backupCount=3  # Number of backup files to keep
    )

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

logger = setup_logger()
