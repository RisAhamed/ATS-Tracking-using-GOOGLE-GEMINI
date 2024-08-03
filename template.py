import os
import logging

# Create the main project folder
project_folder = "ats-project"
if not os.path.exists(project_folder):
    os.makedirs(project_folder)

# Create the subfolders
subfolders = [
    "data",
    "models",
    "code",
    "configs",
    "tests",
    "mlops",
    "mlops/pipelines",
    "mlops/workflows",
    "mlops/monitoring",
    "logs"  # Add the logs folder
]

for subfolder in subfolders:
    folder_path = os.path.join(project_folder, subfolder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

# Create the files
files = [
    ("code", "__init__.py"),
    ("code", "app.py"),
    ("code", "models.py"),
    ("code", "data_processing.py"),
    ("configs", "environment_variables.py"),
    ("configs", "model_configs.py"),
    ("tests", "__init__.py"),
    ("tests", "test_app.py"),
    ("mlops/pipelines", "__init__.py"),
    ("mlops/pipelines", "train_pipeline.py"),
    ("mlops/workflows", "__init__.py"),
    ("mlops/workflows", "train_workflow.py"),
    ("mlops/monitoring", "__init__.py"),
    ("mlops/monitoring", "model_monitoring.py")
]

for folder, file in files:
    file_path = os.path.join(project_folder, folder, file)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass  # Create an empty file
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

# Set up logging
log_folder = os.path.join(project_folder, "logs")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    filename=os.path.join(log_folder, "project.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Project structure created successfully!")