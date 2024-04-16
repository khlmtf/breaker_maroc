import os

# Directory containing the images
directory = "./"

# List files in the directory
files = os.listdir(directory)

# Filter only image files (you can customize this based on your file extensions)
image_files = [file for file in files if file.endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Path for the text file to save the list of image names
output_file = os.path.join(directory, "image_names.txt")

# Write image names to the text file
with open(output_file, 'w') as f:
    for image_file in image_files:
        f.write(image_file + '\n')

print("Image names have been written to:", output_file)

