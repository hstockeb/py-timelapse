# REMEMBER TO INSTALL THE FOLLOWING
# pip install opencv-python
# pip install tqdm


import cv2
import os
from tqdm import tqdm

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory containing the JPG images (same folder as the script)
image_folder = os.path.join(script_dir)  # Update 'path/to/images/' if needed

# List all files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()  # Sort images in alphanumeric order

# Prompt for video resolution
resolution = input("Select video resolution:\n1) 720p\n2) 1080p\n3) 4K\nEnter the number: ")

# Define the width and codec based on selected resolution
if resolution == '1':
    width = 1280
    resolution_name = '720p'
elif resolution == '2':
    width = 1920
    resolution_name = '1080p'
elif resolution == '3':
    width = 3840
    resolution_name = '4K'
else:
    print("Invalid resolution selection. Using default 1080p.")
    width = 1920
    resolution_name = '1080p'

# Prompt for video codec
codec_choice = input("Select video codec:\n1) mp4v\n2) h264\nEnter the number: ")

# Define the codec based on user choice
if codec_choice == '1':
    codec = 'mp4v'
elif codec_choice == '2':
    codec = 'h264'
else:
    print("Invalid codec selection. Using default mp4v.")
    codec = 'mp4v'

# Prompt for video quality
quality = int(input("Enter video quality (0-100): "))
if quality < 0 or quality > 100:
    print("Invalid quality value. Using default value of 70.")
    quality = 70

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*codec)

# Read the first image to get its dimensions
first_image_path = os.path.join(image_folder, images[0])
first_image = cv2.imread(first_image_path)
original_height, original_width, _ = first_image.shape

# Calculate proportional height based on the selected width
height = int((width / original_width) * original_height)

# Create VideoWriter object with calculated dimensions and user-defined quality
video = cv2.VideoWriter(f'output_video_{resolution_name}_{codec}_q{quality}.mp4', fourcc, 24.0, (width, height), isColor=True)

# Iterate through images, resize, and write to video with a progress bar
with tqdm(total=len(images)) as progress_bar:
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        resized_frame = cv2.resize(frame, (width, height))
        video.write(resized_frame)
        progress_bar.update(1)

# Release the VideoWriter and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
