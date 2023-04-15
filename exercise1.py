import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

import cv2
img = cv2.imread('image/a1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', img)
cv2.imshow('Gray image', gray)
