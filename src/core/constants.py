""" Contains the project constants. """

from src.database import schema_dict

BASE_DATA_NAME = 'raw_data.csv'

TARGET_NAME: str = schema_dict['targetColumn']
NUM_COLS: list[str] = schema_dict['numColumnsNames']
CAT_COLS: list[str] = schema_dict['catColumnsNames']
ALL_COLS: list[str] = schema_dict['columnNames']
