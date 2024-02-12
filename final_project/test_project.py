import pytest
from unittest.mock import patch
from PIL import Image
import os
import project



if os.path.exists("test_image.jpg"):
    pass
else:
    img = Image.new(mode="RGB", size=(300, 4000))
    img.save("Test_image.jpg")

def test_resize_image():
    project.resize_image(Image.open("Test_image.jpg"), 100, 100)
    assert os.path.exists("resized_image.jpg")

def test_crop_image():
    project.crop_image(Image.open("Test_image.jpg"), 10, 20, 30, 40)
    assert os.path.exists("cropped_image.jpg")

def test_rotate_image():
    project.rotate_image(Image.open("Test_image.jpg"),45)
    assert os.path.exists("rotated_image.jpg")

def test_apply_grayscale_filter():
    project.apply_grayscale_filter(Image.open("Test_image.jpg"))
    assert os.path.exists("grayscale_image.jpg")

def test_convert_image_format():
    project.convert_image_format(Image.open("Test_image.jpg"), "png")
    assert os.path.exists("Test_image.png")

def test_invalid_choice():
    with patch("builtins.input", side_effect=["6"]):
        with pytest.raises(SystemExit):
            project.main()
