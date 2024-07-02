import streamlit
from PIL import Image

camera_image = streamlit.camera_input("Camera")
print(camera_image)

if camera_image:
    img = Image.open(camera_image)

    gray_image = img.convert("L")

    streamlit.image(gray_image)
