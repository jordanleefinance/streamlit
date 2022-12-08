import streamlit as st
from PIL import Image
import cv2
import os


def load_image(file):
    image = Image.open(file)
    return image

image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])


if image_file is not None:

    with open(os.path.join("C:/tempPhotoDir"), "wb") as f:
        f.write(image_file.getbuffer())
        img = cv2.imread(f, 1)
        print(img)

    # Image to Gray Image

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gray Image to Inverted Gray Image
    inverted_gray_image = 255 - gray_image

    # Blurring The Inverted Gray Image
    blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)

    # Inverting the blurred image
    inverted_blurred_image = 255 - blurred_inverted_gray_image

    # Preparing Photo sketching
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    st.image(load_image(sketch), width=250)


