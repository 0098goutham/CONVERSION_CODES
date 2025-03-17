#Image compress code between 100kb to 100MB 

import os
from PIL import Image

# Remove pixel limit restriction for large images
Image.MAX_IMAGE_PIXELS = None

def compress_images_in_folder(input_folder, output_folder, min_size_kb, max_size_kb):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            if os.path.isfile(input_path):  # Check if it's a valid file
                print(f"Compressing: {filename}")
                compress_image(input_path, output_path, min_size_kb, max_size_kb)
        except Exception as e:
            print(f"Error compressing {filename}: {e}")

def compress_image(input_path, output_path, min_size_kb, max_size_kb):
    try:
        # Open the input image
        img = Image.open(input_path)

        # Resize image if it's too large (maintain aspect ratio)
        max_width, max_height = 1920, 1080  # Desired maximum dimensions
        if img.width > max_width or img.height > max_height:
            img.thumbnail((max_width, max_height))  # Maintains aspect ratio

        # Binary search for optimal quality
        min_quality, max_quality = 1, 95
        final_quality = 95
        size_kb = None

        while min_quality <= max_quality:
            quality = (min_quality + max_quality) // 2
            temp_output = output_path + ".temp"  # Temporary output file for testing size
            img.save(temp_output, "JPEG", quality=quality)
            size_kb = os.path.getsize(temp_output) / 1024  # File size in KB

            if min_size_kb <= size_kb <= max_size_kb:
                final_quality = quality
                break  # Found the ideal size within range
            elif size_kb < min_size_kb:
                max_quality = quality - 1  # Increase quality
            else:
                min_quality = quality + 1  # Reduce quality

        # Save the final compressed image
        img.save(output_path, "JPEG", quality=final_quality)
        print(f"Compressed {os.path.basename(input_path)} to {os.path.basename(output_path)} "
              f"with size {os.path.getsize(output_path) / 1024:.2f} KB")

        # Clean up temporary file
        if os.path.exists(temp_output):
            os.remove(temp_output)

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Example usage
input_folder = r"D:\op-test3"  # Input folder containing images
output_folder = r"D:\compressed op-test"  # Output folder for compressed images
min_size = 100  # Minimum size in KB
max_size = 102400  # Maximum size in KB (100 MB)

compress_images_in_folder(input_folder, output_folder, min_size, max_size)
