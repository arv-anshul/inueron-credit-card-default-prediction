import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal, TypeAlias

RunMode: TypeAlias = Literal['training', 'prediction']
RunId: TypeAlias = str
run_mode_fp = Path('run_mode.config')


@dataclass(init=False)
class Config:
    """ Class for configuration instance attributes. """

    @staticmethod
    def get_run_id() -> RunId:
        """ Get the unique run ID. """
        return datetime.now().strftime('%d%m%y_%H%M%S')

    @staticmethod
    def set_run_mode(mode: RunMode) -> None:
        json.dump({'currentRunMode': mode}, open(run_mode_fp, 'w'))

    @staticmethod
    def get_run_mode() -> RunMode:
        if not run_mode_fp.exists():
            Config.set_run_mode('training')

        return json.load(open(run_mode_fp))['currentRunMode']
