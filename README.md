# Image Processing Toolkit
This repository contains Python scripts designed to handle various image processing tasks. 
It includes functionality to convert SVS (whole slide image) files to JPEG and compress images to optimize storage while maintaining quality.

## Features
1. SVS to JPEG Converter
Converts SVS files (commonly used in pathology imaging) into JPEG format.

Allows downsampling by specifying a factor to reduce the image size while maintaining clarity.

Automatically determines the optimal level for downsampling.

2. Image Compression Tool
Compresses images in a folder to a specified size range (in KB).

Adjusts the image quality and dimensions while maintaining the aspect ratio.

Ideal for reducing image storage requirements without compromising too much on quality.

## Requirements
Python 3.7 or above

Libraries: Pillow, OpenSlide, os

## Install the required libraries using pip: 
  pip install Pillow openslide-python

Do change the folder path as shown in the code/ commented there..
