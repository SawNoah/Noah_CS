import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)


img = st.read('image/a1.jpg')
gray = st.cvtColor(img, cv2.COLOR_BGR2GRAY)

st.imshow('Original image', img)
st.imshow('Gray image', gray)
