import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Streamlit introduction!")

st.write("Display a progress-bar")
st.write("Start")

# tqdm module みたいな奴 ---
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.02)

st.write("Done!!!")
# --- tqdm module みたいな奴

left_column, right_column = st.columns(2)
button = left_column.button("Display text on right column.")
if button:
    right_column.write("There is right column here.")

expander1 = st.expander("query1: hoge")
expander1.write("answer1: hogehoge")
expander2 = st.expander("query2: piyo")
expander2.write("answer2: piyopiyo")
