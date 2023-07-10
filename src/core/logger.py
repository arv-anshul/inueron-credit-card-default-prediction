import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypeAlias

from src.core import run_id, run_mode

LogLevel: TypeAlias = Literal['debug', 'info', 'warn', 'error', 'critical']


@dataclass
class Logger:
    """
    Logger for the project.

    Args:
        logger_name: __name__
        mode: Literal['training', 'prediction']
    """

    logger_name: str

    def __post_init__(self):
        self.logger = logging.getLogger(self.logger_name)
        self.run_id = run_id
        self.logger.setLevel(logging.DEBUG)

        fp = Path(
            f'logs/{run_mode}_logs/{self.run_id}.log'
        )
        fp.parent.mkdir(parents=True, exist_ok=True)

        formatter = logging.Formatter(
            "[ %(asctime)s ] %(filename)s:[%(lineno)d] - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(fp)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, msg: object, *args: object) -> None:
        """Log an info-level message."""
        self.logger.info(msg, *args)

    def exception(self, msg: object, *args: object) -> None:
        """Log an exception-level message."""
        self.logger.exception(msg, *args)

    def log(self, level: LogLevel, msg: object, *args: object) -> None:
        """Log a message with the specified log level."""
        getattr(self.logger, level)(msg, *args)
