from datetime import datetime as dt
from pathlib import Path

from src.core.constants import ALL_COLS, BASE_DATA_NAME, CAT_COLS, NUM_COLS


class PipelineConfig:
    def __init__(self):
        self.root = Path.cwd()
        self.artifact_dir = Path('artifacts', dt.now().strftime('%m%d%y__%H'))
        self.data_schema_fp = self.root / 'src/database/schema.json'
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.artifact_dir.mkdir(parents=True, exist_ok=True)


class DataIngestionConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.base_data_fp = self.root / 'data' / BASE_DATA_NAME
        self.dir = self.artifact_dir / 'data_ingestion'
        self.feature_store_fp = self.dir / 'feature_store' / BASE_DATA_NAME
        self.train_path = self.dir / 'dataset' / 'train.parquet'
        self.test_path = self.dir / 'dataset' / 'test.parquet'
        self.test_size = None   # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(parents=True, exist_ok=True)
        self.feature_store_fp.parent.mkdir(exist_ok=True)
        self.train_path.parent.mkdir(exist_ok=True)
        self.test_path.parent.mkdir(exist_ok=True)


class DataValidationConfig(DataIngestionConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / 'data_validation'
        self.reports_dir = self.root / 'reports'
        self.report_fp = self.reports_dir / 'report.yaml'
        self.missing_threshold = None   # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)


class DataTransformationConfig(DataIngestionConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / 'data_transformation'
        self.transformer_pkl_fp = self.dir / 'transformer.pkl'
        self.target_enc_fp = self.dir / 'target_encoder.pkl'
        self.train_np_path = self.dir / 'transformed_arrays' / 'train.np'
        self.test_np_path = self.dir / 'transformed_arrays' / 'test.np'
        self.all_cols = ALL_COLS
        self.num_cols = NUM_COLS
        self.obj_cols = CAT_COLS
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
        self.train_np_path.parent.mkdir(parents=True, exist_ok=True)


class ModelTrainerConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / 'model_trainer'
        self.model_path = self.dir / 'model.pkl'
        self.expected_training_score = None   # According to project
        self.expected_testing_score = None   # According to project
        self.overfitting_threshold = None   # According to project
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)


class ModelEvaluationConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.change_threshold = None   # According to project


class ModelPusherConfig(PipelineConfig):
    def __init__(self):
        super().__init__()
        self.dir = self.artifact_dir / 'model_pusher'
        self.model_path = self.dir / 'model.pkl'
        self.transformer_path = self.dir / 'transformer.pkl'
        self.target_enc_path = self.dir / 'target_encoder.pkl'
        self.root_stored_model_dir = self.root / 'stored_models'
        self.__create_all_dirs()

    def __create_all_dirs(self):
        self.dir.mkdir(exist_ok=True)
