import streamlit
from PIL import Image

streamlit.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = streamlit.file_uploader("Upload Image")

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

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    streamlit.image(gray_uploaded_img)