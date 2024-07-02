import streamlit
from PIL import Image

with streamlit.expander("Start Camera"):
    camera_image = streamlit.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)

    gray_image = img.convert("L")

    streamlit.image(gray_image)
