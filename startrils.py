import cv2
import numpy as np
import os
from PIL import Image
from tqdm import tqdm

# Get the directory path where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the directory containing your images (same directory as the script)
images_directory = os.path.join(script_directory, 'images')

# Get a list of image file names in the directory
image_files = [os.path.join(images_directory, file) for file in os.listdir(images_directory) if file.endswith('.jpg')]

# Read the first image to get dimensions
first_image = cv2.imread(image_files[0])
height, width = first_image.shape[:2]

# Create an empty numpy array to store the final stacked image
stacked_image = np.zeros((height, width, 3), dtype=np.uint8)

# Prompt user to choose the blending mode
print("Choose a blending mode:")
print("1. Normal")
print("2. Lighten")
selected_mode = input("Enter the mode (1 for Normal, 2 for Lighten): ")

# Loop through each image and blend with the stacked image using the selected blending mode
for image_file in tqdm(image_files, desc='Processing images'):
    image = cv2.imread(image_file)
    if selected_mode == '1':  # Normal blending
        stacked_image = image  # Simply overwrite
    elif selected_mode == '2':  # Lighten blending
        stacked_image = cv2.max(stacked_image, image)  # Lighten mode
    else:
        print("Invalid mode selected. Please choose 1 for Normal or 2 for Lighten.")
        break

# Save the stacked image based on the selected blending mode
if selected_mode == '1':
    output_file_path = os.path.join(script_directory, 'stacked_startrail_normal.jpg')
elif selected_mode == '2':
    output_file_path = os.path.join(script_directory, 'stacked_startrail_lighten.jpg')
else:
    output_file_path = ''

if output_file_path:
    cv2.imwrite(output_file_path, stacked_image)
    print(f"Stacked image saved as {output_file_path}")
