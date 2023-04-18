#Stream Basic Functions
import streamlit as st

#Title
st.title("Hello Streamlit")

#Header
st.header("This is a header")

#subheader
st.subheader("This is subheader")

#Text
st.text("Hello Welcome to Streamlit!!")

# success
st.success("Success Message")

#Info
st.info("Information")

#Warning
st.warning("Warning Message")

#Error
st.error("Error Message")

#Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

#Write Text
st.write("Text with write")

#Using write function, we can also display code in coding format.
# This is not possible using st.text().
#Writing python inbuilt function range()
st.write(range(10))

#Stream Basic Function
import streamlit as st
from PIL import Image

#Display Images:
img = Image.open("image/laptop.png")

#display image using streamlit
#width is used to set the width of an image
st.image(img, width=200)

#checkbox
#A checkbox returns a boolean value.
#When the box is checked, it returns a True value
#else returns a Flase value.

#check if the checkbox is checked
# title of the checkbox is "Show/Hide"
if st.checkbox("Show/Hide"):
  #display the text if the checkbox returns True value
  st.text("Showing the widget")
  st.image(img,width=50)
  
#radio button
#first rgument is the title of the radio button
#second argument is the options for the radio button
status = st.radio("Select Gender:", ('Male',"Female"))
#conditional statement to print
#Male if male is selected else print female
#show the result using the success function
st.success(status)
