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
