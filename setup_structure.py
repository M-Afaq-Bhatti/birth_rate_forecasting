import os

# Define the folder and file structure
structure = {
    "data": ["raw/", "processed/"],
    "notebooks": ["model_dev.ipynb", "data_cleaning.ipynb"],
    "src": [
        "__init__.py",
        "config.py",
        "data_ingestion.py",
        "preprocessing.py",
        "model.py",
        "forecasting.py",
        "visualizations.py",
        "utils.py"
    ],
    "app": [
        "dashboard.py",
        "pages/scenario_simulator.py",
        "assets/"
    ],
    "scheduler": ["update_data.py", "retrain_model.py"],
    "reports": [],
    "tests": ["test_model.py"],
    ".github/workflows": ["cron.yml"],
}

# Root-level files
root_files = [
    "Dockerfile",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "LICENSE"
]

# Function to create folders and files
def create_structure(base_path="."):
    for folder, items in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for item in items:
            item_path = os.path.join(folder_path, item)
            if item.endswith("/"):
                os.makedirs(item_path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(item_path), exist_ok=True)
                with open(item_path, "w") as f:
                    f.write("")  # Create empty file

    # Create root-level files
    for file in root_files:
        with open(os.path.join(base_path, file), "w") as f:
            f.write("")

    print("✅ Folder structure created successfully!")

# Run the script
if __name__ == "__main__":
    create_structure()
