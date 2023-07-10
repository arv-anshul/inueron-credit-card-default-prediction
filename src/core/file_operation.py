from dataclasses import dataclass
from pathlib import Path

import dill
import numpy as np

from src.core.logger import Logger

logger = Logger(__name__)


@dataclass
class FileOperation:
    """ Initialize the FileOperation class. """

    def dump_model(self, model: object, fp: Path) -> None:
        with open(fp, 'wb') as f:
            dill.dump(model, f)
        logger.info('Model %s dumped.', fp)

    def load_model(self, fp: Path) -> object:
        with open(fp, 'rb') as f:
            logger.info('Model %s loaded.', fp)
            return dill.load(f)

    def dump_array(self, array: np.ndarray, fp: Path) -> None:
        array.dump(fp)
        logger.info('Array %s dumped.', fp)

    def load_array(self, fp: Path) -> np.ndarray:
        logger.info('Array %s loaded.', fp)
        return np.load(fp)
