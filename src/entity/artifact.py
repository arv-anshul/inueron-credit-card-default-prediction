""" Entity for artifact folder to store all data and models. """

from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    feature_store_fp: Path
    train_path: Path
    test_path: Path


@dataclass
class DataValidationArtifact(DataIngestionArtifact):
    report_fp: Path


@dataclass
class DataTransformationArtifact:
    transformer_pkl: Path
    target_enc_fp: Path
    train_npz_path: Path
    test_npz_path: Path


@dataclass
class ModelTrainerArtifact:
    model_path: Path
    train_score: float
    test_score: float


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool
    improved_accuracy: float


@dataclass
class ModelPusherArtifact:
    self_dir: Path
    stored_model_dir: Path
