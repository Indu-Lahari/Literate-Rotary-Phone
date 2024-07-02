import streamlit
from PIL import Image

camera_image = streamlit.camera_input("Camera")
print(camera_image)

img = Image.open(camera_image)

gray_image = img.convert("L")
