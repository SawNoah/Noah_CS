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
