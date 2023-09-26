# EPUB Compressor

EPUB Compressor is a simple yet powerful application designed to help you compress EPUB files efficiently. With EPUB Compressor, you can easily reduce the size of your EPUB files by a specified compression percentage, making them more suitable for sharing, storage, or distribution. This application comes with a user-friendly graphical user interface (GUI) that makes the compression process straightforward and accessible to users of all skill levels.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Using the GUI](#using-the-gui)
  - [Command Line Usage](#command-line-usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before using EPUB Compressor, ensure that you have the following prerequisites installed on your computer:

- **Windows Operating System**: EPUB Compressor is currently supported on Windows.

### Installation

To use EPUB Compressor, follow these steps:

1. Download the EPUB Compressor executable (`epub-compressor.exe`) from the [GitHub releases page](https://github.com/your-username/your-repo/releases).

2. Place the `epub-compressor.exe` file in a directory of your choice.

3. You're ready to start compressing EPUB files!

## Usage

EPUB Compressor can be used in two ways: through the graphical user interface (GUI) or via the command line. Choose the method that best suits your needs.

### Running the Application

1. Double-click the `epub-compressor.exe` file to launch the EPUB Compressor GUI.

2. Use the GUI to specify the following settings:
   - **Input Folder**: The folder containing the EPUB files you want to compress.
   - **Compression Percentage**: The desired level of compression as a percentage.
   - **Output Folder**: (Optional) The folder where you want the compressed EPUB files to be saved. If left empty, the compressed files will be stored in the same directory as the original files.

3. Click the "Compress" button to start the compression process.

4. EPUB Compressor will process the EPUB files in the input folder, applying the specified compression level, and save the compressed files in the output folder (if provided) or the original folder.

### Using the GUI

The GUI provides a user-friendly interface for compressing EPUB files:

![EPUB Compressor GUI](gui-screenshot.png)

- **Input Folder**: Click the "Browse" button to select the folder containing your EPUB files.

- **Compression Percentage**: Enter the desired compression percentage. For example, entering "50" will compress the EPUB files by 50%.

- **Output Folder**: (Optional) Click the "Browse" button to choose a different folder to save the compressed EPUB files. If left empty, the compressed files will be saved in the same folder as the original files.

- **Compress Button**: Click this button to start the compression process.

### Command Line Usage

EPUB Compressor can also be used from the command line, allowing for automation and scripting. Here's how to use it:

```plaintext
epub-compressor.exe --input <input_folder> --percentage <compression_percentage> [--output <output_folder>]
```

- `<input_folder>`: The folder containing the EPUB files you want to compress.

- `<compression_percentage>`: The desired level of compression as a percentage.

- `<output_folder>` (optional): The folder where you want the compressed EPUB files to be saved. If not specified, the compressed files will be stored in the same folder as the original files.

Example:

```plaintext
epub-compressor.exe --input "C:\MyEbooks" --percentage 30 --output "C:\CompressedEbooks"
```

## Contributing

Thank you for considering contributing to EPUB Compressor! If you'd like to contribute, please fork the repository, create a new branch, make your changes, and then submit a pull request. You can also report issues on the [GitHub Issues page](https://github.com/your-username/your-repo/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
