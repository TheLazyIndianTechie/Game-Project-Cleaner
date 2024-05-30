# 🧹 Game Project Cleaner

A simple command line tool to clean up Library, Intermediate, and other folders in Unreal Engine, Unity, and Godot projects based on search queries.

## ✨ Features

- 🔍 Recursively scans specified directories for matching folders.
- ⏳ Displays progress for each step using `tqdm`.
- 📂 Allows users to select the base directory through a popup dialog.
- ❗ Prompts for user confirmation before deleting directories.
- 🛠️ Supports scanning and cleaning specific files for Unity, Unreal, and Godot based on user input.
- 📋 Maintains separate lists for files to be scanned and ignored for each engine.

## ⚠️ Warning

<div style="border: 2px solid red; padding: 10px; background-color: yellow; color: red; font-size: 18px; font-weight: bold;">
  <b>USE THIS TOOL AT YOUR OWN RISK:</b> 
   This script will permanently delete directories that match the search term. Ensure you review the directories listed before confirming deletion. The author is not responsible for any data loss or unintended deletions.
</div>

## 🛠️ Requirements

- 🐍 Python 3.x
- `colorama==0.4.6`
- `tqdm==4.66.4`

## 🚀 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TheLazyIndianTechie/GameProjectCleaner.git
   cd GameProjectCleaner
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
5. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```
## 📄 Usage

1. Run the script:
   python app.py

2. Follow the prompts:
   - Select the base directory.
   - Choose the type of project to clean (Unity, Unreal, or Godot).
   - Enter the search term to match directories.
   - Confirm deletion of matched directories.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## 👤 Author

- **TheLazyIndianTechie** - [GitHub](https://github.com/TheLazyIndianTechie)
