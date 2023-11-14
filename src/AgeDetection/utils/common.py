# Importing the modules
import os
from box.exceptions import BoxValueError
import yaml
from AgeDetection import logger  
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Defining Utility functions
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Empty file.

    Returns:
        ConfigBox: ConfigBox containing the YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of paths for directories to be created.
        verbose (bool, optional): Whether to log created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves JSON data to a file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data to a file using joblib.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    """Decodes a base64-encoded image string and saves it to a file.

    Args:
        imgstring (str): Base64-encoded image string.
        fileName (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file into base64.

    Args:
        croppedImagePath (str): Path to the image file to be encoded.

    Returns:
        str: Base64-encoded image string.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
