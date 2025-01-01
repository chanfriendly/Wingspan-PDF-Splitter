import subprocess
import sys
import shutil
import os
from pdf2image import convert_from_path, exceptions

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_poppler():
    print("Poppler not found. Installing via Homebrew...")
    subprocess.check_call(["brew", "install", "poppler"])

# Ensure required packages are installed
try:
    from pdf2image import convert_from_path
except ImportError:
    print("pdf2image not found, installing...")
    install_package("pdf2image")
    from pdf2image import convert_from_path

# Ensure poppler-utils is installed
if not shutil.which("pdftoppm"):
    if sys.platform == "darwin":  # macOS
        install_poppler()
    else:
        print("Poppler is required but not found. Please install it manually.")
        sys.exit(1)

# Input and output paths
input_folder = # Change to your folder of unsplit PDFs
output_folder = # Change to your directory for completed PDF splits
# Choose format: "JPEG" or "PNG"
output_format = "JPEG"  # Change to "PNG" if you prefer PNG format

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each PDF file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.pdf'):
        input_path = os.path.join(input_folder, filename)
        try:
            # Get the PDF name without extension
            pdf_name = os.path.splitext(filename)[0]
            
            # Convert PDF pages to images
            images = convert_from_path(input_path, dpi=300)
            
            # Save each page as an individual image
            for page_num, image in enumerate(images, start=1):
                if output_format == "JPEG":
                    output_path = os.path.join(output_folder, f"{pdf_name}_page_{page_num}.jpg")
                    image.save(output_path, "JPEG", quality=95)  # Quality ranges from 1 (worst) to 95 (best)
                else:
                    output_path = os.path.join(output_folder, f"{pdf_name}_page_{page_num}.png")
                    image.save(output_path, "PNG")
            
            print(f"Successfully processed: {filename}")
            
        except exceptions.PDFPageCountError as e:
            print(f"Error processing {filename}: Unable to get page count. The PDF might be corrupted.")
            print(e)
            continue
        except Exception as e:
            print(f"An unexpected error occurred with {filename}: {e}")
            continue

print(f"Processing completed. Images are saved in '{output_folder}'.")
