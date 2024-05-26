# Python program to find the size(resolution) of a Image.

from PIL import Image

def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Unable to open image. Error: {e}")
        return None

if __name__ == "__main__":
    
    image_path = 'D:\Wallpapers\IMG20230409081838.jpg'
    
    size = get_image_size(image_path)
    
    if size:
        print(f"Resolution of the image is {size[0]}x{size[1]} pixels.")
    else:
        print("Failed to get the image size.")
