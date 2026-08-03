"""Core functionality for the forensic logging package.

This module provides helper functions for creating and configuring loggers.
"""
import logging
from time import gmtime
from logging import Logger
from pathlib import Path
from datetime import datetime, timezone


class UTCFormatter(logging.Formatter):
    converter = gmtime

def forensic_logger(name: str,
                 logfile_path: Path | None = None,
                 level: str | int = logging.INFO,
                 console: bool = False,
                 timestamp: bool = False,
                 verbose: bool = False) -> Logger:
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

    create and set up a logger with path "log/", optional timestamp and optional console logging
    """

    logging_format = "%(asctime)s %(levelname)-6s %(filename)s [%(funcName)s] - %(message)s"

    if isinstance(level, str):
        level_name = level.upper()
        # Use public API to check for level existence
        valid_levels = logging.getLevelNamesMapping() if hasattr(logging, "getLevelNamesMapping") else logging._nameToLevel
        if level_name not in valid_levels:
            raise ValueError(f"Invalid logging level: {level}")
        level = getattr(logging, level_name, logging.INFO)


    if logfile_path is None:
        log_path = Path.cwd() / 'log' # default log directory is "log/"
        log_path.mkdir(parents=True, exist_ok=True)

        timestamp_str = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f") if timestamp else ''
        filename = f'{timestamp_str}_{name}.log' if timestamp else f'{name}.log'
        logfile_path = log_path / filename
        if verbose:
            print(f'logfile path set to: {logfile_path}')

    if verbose:
        print(f'logfile path: {logfile_path}; level: {level}; console: {console}; timestamp: {timestamp}; verbose: {verbose}')


    logger = logging.getLogger(name)
    logger.setLevel(level)

    has_file_handler = any(
        isinstance(h, logging.FileHandler)
        for h in logger.handlers
    )

    if not has_file_handler:
        if verbose:
            print(f'creating logger {name}')

        try:
            file_handler = logging.FileHandler(logfile_path, encoding='utf-8')
        except OSError as e:
            raise RuntimeError(f'Error creating file handler for {logfile_path}: {e}') from e

        file_handler.setLevel(level)

        formatter = UTCFormatter(logging_format)

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # optional console output
        if console:
            if verbose:
                print(f'forensic-logger: creating logger {name} (console)')
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level)
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    logger.propagate = False
    return logger
