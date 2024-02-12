from PIL import Image, ImageFilter, ImageOps
import sys
import os

def main():
    print('\n[+]Welcome to Image processing\n')
    while True:
        print("\n[1] Resize a image\n[2] Crop a image\n[3] Rotate the image\n[4] Apply grayscale filter\n[5] Convert image format\n[6] Exit")
        choice = int(input("\n[+]Enter your choice: "))

        if choice not in [1,2,3,4,5,6]:
            print("\n[-]Invalid choice")
            continue

        elif choice == 1:
            try:
                resize_image(take_input(),int(input("\n[+]Enter the width: ")),int(input("\n[+]Enter the height: ")))
            except:
                print("[-] Something went Wrong")
                continue

        elif choice == 2:
            try:
                crop_image(take_input(),int(input("\n[+]Enter the left: ")), int(input("\n[+]Enter the top: ")), int(input("\n[+]Enter the right: ")),int(input("\n[+]Enter the bottom: ")))
            except:
                print("[-] Something went Wrong")
                continue

        elif choice == 3:
            try:
                rotate_image(take_input(),int(input("\n[+]Enter the angle: ")))
            except:
                print("[-] Something went Wrong")
                continue

        elif choice == 4:
            try:
                apply_grayscale_filter(take_input())
            except:
                print("[-] Something went Wrong")
                continue

        elif choice == 5:
            try:
                convert_image_format(take_input(), input("\n[+]Enter the new format (jpg, png, etc.): "))
            except:
                print("[-] Something went Wrong")
                continue

        elif choice == 6:
            sys.exit("\n[+]Thank you for using this program")

def take_input():
    user_input = input("\n[+]Enter the path of image: ")
    while True:
        try:
            image = Image.open(user_input)
            break
        except:
            print("\n[-]Invalid path")
            user_input = input("\n[+]Enter the path of image: ")
            continue
    return image

def resize_image(image,width=0,height=0):
    print("[+]Image size: ",image.size)
    new_image = image.resize((width,height))
    new_image.save("resized_image.jpg")
    print("\n[+]Image resized successfully")

def crop_image(image,left=0,top=0,right =0,bottom=0):
    print("[+]Image size: ",image.size)
    new_image = image.crop((left,top,right,bottom))
    new_image.save("cropped_image.jpg")
    print("\n[+]Image cropped successfully")

def rotate_image(image ,angle=0):
    print("[+]Image size: ",image.size)
    new_image = image.rotate(angle)
    new_image.save("rotated_image.jpg")
    print("\n[+]Image rotated successfully")

def apply_grayscale_filter(image):
    print("[+]Applying grayscale filter")
    new_image = image.convert("L")
    new_image.save("grayscale_image.jpg")
    print("\n[+]Image filter applied successfully")

def convert_image_format(image, new_format):
    print("[+]Converting image format")
    root, ext = os.path.splitext(image.filename)
    new_image = image.save(f"{root}.{new_format}")
    print("\n[+]Image format converted successfully")

if __name__ == "__main__":
    main()
 