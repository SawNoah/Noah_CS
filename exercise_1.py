#Stream Basic Functions
import streamlit as st

#Title
st.title("Hello Streamlit")

#Header
st.header("Exercise 1")

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

st.header("Exercise 2")
#Stream Basic Function
import streamlit as st
from PIL import Image

#Display Images:
img = Image.open("image/laptop.jpg")

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

st.header("Exercise 3")
esub - t.selectbox("Elective:",
                   ["Music","Japanese","Korea"])
st.write("Your elective subject is:",esub)

hobbies = st.multiselect("Hobbies:",
                         ["Painting","Dancing","Sports","Gaming"])

st.write("You select:", len(hobbies),'hobbies')

if(st.button("Click me. Click me")):
  st.text("Hello! Welcome to Stremlit")
  
name = st.text_input("Enter your name:", "Type Here ...")

if (st.button("Submit")):
   result = name.title()
   st.write('Hello',result)
   
level = st.slider("Select the level", 1,10)
st.text("Selected: {}", format(level)) 
   
