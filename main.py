import streamlit
from PIL import Image

#Start the camera
with streamlit.expander("Start Camera"):
    camera_image = streamlit.camera_input("Camera")

if camera_image:
    #Create the Pillow Image instance
    img = Image.open(camera_image)

    #Convert the Pillow Image to grayscale
    gray_image = img.convert("L")

    #Render the grayscale image to the webpage
    streamlit.image(gray_image)
