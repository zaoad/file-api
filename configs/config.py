# config/config.py

from functools import lru_cache
from typing import Any, Dict, List
from pydantic import BaseSettings
import logging


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        project_name (str): The name of the project.
        project_description (str): A brief description of the project.
        clamav_config_file_path (str): Path to the ClamAV config file.
        clamav_scanned_dir (str): Directory for ClamAV scanned files.
        max_file_size (int): Maximum file size allowed for processing.
        yara_rule_packages (str): Path to Yara rule packages.
        secret_key (str): Secret key for JWT generation.
        algorithm (str): Algorithm for JWT encoding.
        api_tokens (List[Dict[str, Any]]): List of API tokens.
        expiration_time_minutes (int): Token expiration time in minutes.
        issuer (str): JWT token issuer.
        cron_schedule (str): Cron schedule for periodic tasks.
        allowed_filetypes (str): Allowed file types for processing.
    """

    project_name: str = "FileAPI Processor"
    project_description: str = (
        "Sanitization and Validation, Malware Scanning, OCR and NER Processing, File Optimization"
    )
    clamav_config_file_path: str
    clamav_scanned_dir: str
    max_file_size: int
    yara_rule_packages: str = "/ziv/shared/packages/yara_rules.yar"
    secret_key: str
    algorithm: str
    api_tokens: List[Dict[str, Any]]
    expiration_time_minutes: int
    issuer: str
    cron_schedule: str
    allowed_filetypes: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    """
    Returns a cached instance of the Settings object.

    Returns:
        Settings: The application settings.
    """
    logging.info("Fetching application settings.")
    return Settings()


settings = get_settings()
logging.info("Configuration loaded successfully.")
