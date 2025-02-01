import os
from pathlib import Path

print(Path("a/b/c.txt"))
list_of_files=[
    ".github/workflows",
    "src/__init__.py",
    "src/Components/__init__.py"
    "src/Components/data_ingestion.py",
    "src/Components/data_transformation.py",
    "src/Components/model_trainer.py",
    "src/Components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]
for file_path in list_of_files:
    file_path = Path(file_path)

    # Create parent directories if they don't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create empty files if they don't exist
    if not file_path.exists():
        file_path.touch()
        print(f"Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")