import streamlit as st
x = st.slider("Select a value")
answer = x, "squared is", x * x
st.warning(answer)

import streamlit as st
from PIL import Image
img = Image.open("image/a1.jpg")
st.image(img,width=200)

if st.checkbox("Show/Hide"):
  st.text("Showing the widget")
  st.image(img,width=50)

status = st.radio("select gender:", ('Male','Female'))
st.success(status)

#Import libraries
import streamlit as st
import numpy as np
from  PIL import Image, ImageEnhance

#Add file uploader to allow users to upload photos
fileTypes = ["jpeg", "png", "jpg"]
file = st.file_uploader("Upload  image file",type=fileTypes)
if file is not None:
    st.image(file)

    import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
    cv2.imwrite("captured_image.jpg", cv2_img)
