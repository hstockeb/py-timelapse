import cv2
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory containing the JPG images (same folder as the script)
image_folder = os.path.join(script_dir)  # Update 'path/to/images/' if needed

# List all files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()  # Sort images in alphanumeric order

# Define the width for 4K resolution
width_4k = 3840

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed

# Read the first image to get its dimensions
first_image_path = os.path.join(image_folder, images[0])
first_image = cv2.imread(first_image_path)
original_height, original_width, _ = first_image.shape

# Calculate proportional height based on the 4K width
height_4k = int((width_4k / original_width) * original_height)

# Create VideoWriter object with calculated dimensions
video = cv2.VideoWriter('output_video.mp4', fourcc, 24.0, (width_4k, height_4k))

# Iterate through images, resize, and write to video
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    resized_frame = cv2.resize(frame, (width_4k, height_4k))
    video.write(resized_frame)

# Release the VideoWriter and close all OpenCV windows
video.release()
cv2.destroyAllWindows()