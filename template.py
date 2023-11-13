# Import necessary libraries
import os
from pathlib import Path
import logging

# Configure logging to provide information
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = 'AgeDetection'

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # Create a .gitkeep file inside the .github/workflows directory
    f"src/{project_name}/__init__.py",  # Create an __init__.py file inside the src/cnnClassifier directory
    f"src/{project_name}/components/__init__.py",  # Create an __init__.py file inside the components directory
    f"src/{project_name}/utils/__init__.py",  # Create an __init__.py file inside the utils directory
    f"src/{project_name}/config/__init__.py",  # Create an __init__.py file inside the config directory
    f"src/{project_name}/config/configuration.py",  # Create a configuration.py file inside the config directory
    f"src/{project_name}/pipeline/__init__.py",  # Create an __init__.py file inside the pipeline directory
    f"src/{project_name}/entity/__init__.py",  # Create an __init__.py file inside the entity directory
    f"src/{project_name}/constants/__init__.py",  # Create an __init__.py file inside the constants directory
    "config/config.yaml",  # Create a config.yaml file inside the config directory
    "dvc.yaml",  # Create a dvc.yaml file
    "params.yaml",  # Create a params.yaml file
    "requirements.txt",  # Create a requirements.txt file
    "setup.py",  # Create a setup.py file
    "research/trials.ipynb",  # Create a trials.ipynb file inside the research directory
    "templates/index.html"  # Create an index.html file inside the templates directory
]

# Iterate through the list of files and directories
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path into a Path object for easier manipulation
    filedir, filename = os.path.split(filepath)  # Split the file path into its directory and filename

    # Check if the directory name is not an empty string
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist, with exist_ok=True to avoid errors
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log the creation of the directory

    # Check if the file does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file at the specified path
        logging.info(f"Creating empty file: {filepath}")  # Log the creation of the empty file

    else:
        logging.info(f"{filename} is already exists")  # Log that the file already exists
