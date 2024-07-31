from PIL import Image
# Open an image file
img = Image.open('input_image.jpeg')
# Calculate the width and height of the image
width, height = img.size
# Create two new images, each half the width of the original
img1 = img.crop((0, 0, width//2, height))
img2 = img.crop((width//2, 0, width, height))
# Save the images
img1.save('output_image_1.jpg')
img2.save('output_image_2.jpg')
