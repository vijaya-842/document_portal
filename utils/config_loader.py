import os
from pathlib import Path

import yaml


def load_config(config_path: str | None = None) -> dict:
    """Load config.yaml. Defaults to <project root>/config/config.yaml."""
    if config_path is None:
        config_path = os.getenv("CONFIG_PATH") or (
            Path(__file__).resolve().parent.parent / "config" / "config.yaml"
        )
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}