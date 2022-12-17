from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    BASE_DIR: Path
    DATA_DIR: Path


base_dir = Path(__file__).resolve().parent

settings = Settings(
    BASE_DIR=base_dir,
    DATA_DIR=base_dir / "data",
)
