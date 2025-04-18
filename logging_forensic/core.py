import logging
from pathlib import Path
from datetime import datetime

def forensic_logger(name: str,
                 logfile_path: Path = None,
                 level=logging.INFO,
                 console: bool = False,
                 timestamp: bool = False,
                 verbose: bool = False) -> logging.Logger:

    if verbose:
        print(f'forensic-logger: logfile path: {logfile_path}; level: {level}; console: {console}; timestamp: {timestamp}; verbose: {verbose}')

    """
    create and setup a logger with path "../log/",optional timestamp and optional console logging
    :param name: name of the logger
    :param logfile_path: path to log file
    :param level: logging level
    :param console: if true console logging
    :return: logger object
    """

    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    if logfile_path is None:
        base_path = Path.cwd() / 'log' # default log directory is "log/"
        base_path.mkdir(parents=True, exist_ok=True)

        timestring = datetime.now().strftime("%Y%m%d-%H%M%S") if timestamp else ''
        filename = f'{timestring}_{name}.log' if timestamp else f'{name}.log'
        logfile_path = base_path / filename
        if verbose:
            print(f'forensic-logger: logfile_path set to: {logfile_path} ')

    if verbose:
        print(f'forensic-logger: log file path is {logfile_path}')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        if verbose:
            print(f'forensic-logger: creating logger {name}')
        file_handler = logging.FileHandler(logfile_path)
        file_handler.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # optional console output
        if console:
            if verbose:
                print(f'forensic-logger creating logger {name} (console)')
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level)
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    logger.propagate = False
    return logger
