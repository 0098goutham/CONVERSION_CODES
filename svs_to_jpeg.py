##THIS CODE IS USING PYTHON LANG##
#This is done with the help of ai tools and locally sourced codes..

import os
import openslide
from PIL import Image

def convert_svs_to_jpg(input_folder, output_folder, downsample_factor=64):
    # Print the current working directory for debugging purposes
    print("Current working directory:", os.getcwd())
    
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please check the path.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.svs'):
            svs_path = os.path.join(input_folder, filename)
            try:
                # Open the whole slide image
                slide = openslide.OpenSlide(svs_path)
                
                # Determine the optimal level for downsampling using the provided factor
                level = slide.get_best_level_for_downsample(downsample_factor)
                level_dims = slide.level_dimensions[level]
                
                # Read the entire region at the selected level
                region = slide.read_region((0, 0), level, level_dims)
                
                # Convert to RGB (to save as JPEG)
                region = region.convert("RGB")
                
                # Define the output JPEG file path
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_path = os.path.join(output_folder, jpg_filename)
                
                # Save the image as a JPEG
                region.save(jpg_path, "JPEG", quality=85)
                print(f"Converted {filename} -> {jpg_filename}")
                
                slide.close()
            except Exception as e:
                print(f"Error processing {svs_path}: {e}")

if __name__ == "__main__":
    # Define the input and output directories (adjust paths if needed)
    input_dir = "D:\I-p-test2"   # Folder where your SVS files are located 
    output_dir = "D:\op-test3"  # Folder where JPEGs will be saved
    convert_svs_to_jpg(input_dir, output_dir, downsample_factor=64)



