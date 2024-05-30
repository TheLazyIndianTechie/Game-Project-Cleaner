
# Unreal Unity Cleanup Tool

A simple command line tool to clean up Library, Intermediate, and other folders in Unreal Engine and Unity projects based on search queries.

## Features

- Recursively scans specified directories for matching folders.
- Displays progress for each step using `tqdm`.
- Allows users to select the base directory through a popup dialog.
- Prompts for user confirmation before deleting directories.

## Requirements

- Python 3.x
- `tqdm` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TheLazyIndianTechie/UnrealUnityCleanupTool.git
   cd UnrealUnityCleanupTool
   ```

2. Install the required library:
   ```sh
   pip install tqdm
   ```

## Usage

1. Run the script:
   ```sh
   python app.py
   ```

2. Follow the prompts:
   - Select the base directory.
   - Enter the search term to match directories.
   - Confirm deletion of matched directories.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## Author

- **The Lazy Indian Techie** - [GitHub](https://github.com/TheLazyIndianTechie)

## Acknowledgments

- Inspired by the need to manage Unreal Engine and Unity project directories efficiently.
