"""A utility function to create and configure a customizable forensic logger.

This function enables the creation of a logger with various options such as
logging to a specified file, setting a logging level, enabling console
output, appending timestamps to log filenames, and verbosity for debugging
purposes. The logger is designed to streamline file-based logging in
structured applications with minimal configuration.

:param name: The name of the logger.
:type name: str
:param logfile_path: The path to the log file. Defaults to a generated file
    inside the "log" directory within the current working directory.
:type logfile_path: Path, optional
:param level: The logging level for the logger, which may be specified as
    a string or `logging` level constant. Defaults to `logging.INFO`.
:type level: typing.Union[str, int], optional
:param console: If True, a console handler is added for logging to the
    standard output. Defaults to False.
:type console: bool, optional
:param timestamp: If True, a timestamped filename is generated for the log
    file. Defaults to False.
:type timestamp: bool, optional
:param verbose: Enables verbose console debugging output during the logger
    setup process. Defaults to False.
:type verbose: bool, optional

:return: A configured logger instance.
:rtype: logging.Logger
"""
import logging
from typing import Union
from pathlib import Path
from datetime import datetime

def forensic_logger(name: str,
                 logfile_path: Path = None,
                 level: Union[str, int] = logging.INFO,
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
