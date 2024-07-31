import os
import argparse
from PIL import Image

def split_image(input_path):
    img = Image.open(input_path)
    width, height = img.size
    
    # Create two new images, each half the width of the original
    img_left = img.crop((0, 0, width // 2, height))
    img_right = img.crop((width // 2, 0, width, height))
    
    # Get the base name and extension of the input file
    base_name, ext = os.path.splitext(input_path)
    
    output_path_left = f'{base_name}_left{ext}'
    output_path_right = f'{base_name}_right{ext}'
    
    img_left.save(output_path_left)
    img_right.save(output_path_right)
    
    print(f'Images saved as {output_path_left} and {output_path_right}')

def main():
    parser = argparse.ArgumentParser(description='Split an image into two halves.')
    parser.add_argument('input_image_path', type=str, help='Path to the input image file')
    args = parser.parse_args()
    split_image(args.input_image_path)

if __name__ == "__main__":
    main()
