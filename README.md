# PDF Page Splitter and Image Converter

This Python script takes a folder of PDF files and converts each page into individual image files (JPEG or PNG format). It's particularly useful for breaking down multi-page PDFs into separate images while maintaining high quality. It was intended for helping a friend with Wingspan custom cards, however it can be used for any PDF you want to split.

## Prerequisites

- Python 3.x
- macOS (for Homebrew installation of Poppler) or Linux
- Required Python packages (automatically installed by the script):
  - pdf2image
- Poppler (automatically installed via Homebrew on macOS)
- If using for Wingspan, I've already compiled all the available PDFs as of 1/1/25 in this [Google Drive ]([url](https://drive.google.com/drive/folders/1UTNUvOgeOwFbyanAUCNlvl_Eo0wcSMbF?usp=sharing)), both split and not split. I plan on making a tool similar to [MPCFill]([url](https://mpcfill.com/)) to make automating uploads a breeze.
-   Note that there are two PDFS that made cards a 3x3 grid instead of each card on its own page. I haven't resolved these yet.

## Installation

1. Clone or download the script to your local machine
2. Ensure Python 3.x is installed on your system
3. The script will automatically install required dependencies on first run

## Configuration

Before running the script, modify these variables in the script to match your setup:

```python
input_folder = [Directory of your unsplit PDFs]
output_folder = [Where you want your split PDFs to end up]
output_format = "JPEG"  # Change to "PNG" if preferred
```

## Usage

1. Place your PDF files in the input folder
2. Run the script:
   ```bash
   python split_multiple_pdfs.py
   ```
3. The script will:
   - Process each PDF in the input folder
   - Convert each page to an image
   - Save images in the output folder using the format: `original_filename_page_X.jpg/png`

## Output Options

### JPEG Format
- Default quality is set to 95 (high quality)
- Produces smaller file sizes
- Better for photographs and complex images
- File extension: .jpg

### PNG Format
- Lossless compression
- Better for text and graphics
- Larger file sizes
- File extension: .png

## Error Handling

The script includes error handling for:
- Corrupted PDF files
- Invalid PDF formats
- Missing dependencies
- File access issues

If an error occurs with one PDF, the script will continue processing the remaining files.

## Customization

To modify image quality settings:

For JPEG:
```python
image.save(output_path, "JPEG", quality=95)  # Adjust quality (1-95)
```

For DPI (resolution):
```python
images = convert_from_path(input_path, dpi=300)  # Adjust DPI as needed
```

## Troubleshooting

1. If you get "Poppler not found" error:
   - On macOS: The script will attempt to install via Homebrew
   - On Linux: Install poppler-utils manually

2. If you get permission errors:
   - Ensure you have read access to the input folder
   - Ensure you have write access to the output folder

3. If PDFs fail to process:
   - Verify the PDF files aren't corrupted
   - Try processing a single known-good PDF first

## License

This script is provided as-is for free use and modification.

## Support

For issues or questions:
1. Check the error messages in the console output
2. Verify all prerequisites are installed
3. Ensure paths are correctly set in the script
