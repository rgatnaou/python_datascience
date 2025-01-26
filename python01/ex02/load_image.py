from PIL import Image
img = Image.open('landscape.jpg')

# Get the image size (width, height)
width, height = img.size

# Get the number of channels (mode determines the channels)
if img.mode == 'RGB':
    channels = 3
elif img.mode == 'RGBA':
    channels = 4
else:
    channels = 1  # For grayscale images
pixels = list(img.getdata())
# unique_colors = list(set(pixels))
# Print the size in (height, width, channels) format
print(f"Image size: ({height}, {width}, {channels})")
print(pixels[:10])


# from PIL import Image
# import numpy as np

# # Open the image using Pillow
# img = Image.open('image.jpg')

# # Convert to RGB (in case it's in another mode, like RGBA or grayscale)
# img_rgb = img.convert('RGB')

# # Convert the image to a NumPy array (this gives a 3D array)
# img_array = np.array(img_rgb)

# # img_array now has the shape (height, width, 3) with RGB values for each pixel
# print(img_array.shape)  # This will print the shape of the array
# print(img_array)        # This will print the RGB values of the image
