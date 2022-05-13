
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

with open("pipe.pkl", "rb") as a:
    pipeline = pickle.load(a)

    
df = pd.read_csv('gender_classification.csv') 

st.header("Gender Classification")
st.subheader("by Anita")

img = Image.open('gambar_gender.png')

columns =  ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide', 'nose_long', 'lips_thin', 'distance_nose_to_lip_long']

# ============= INPUT =============

long_hair= st.number_input("long_hair")
forehead_width_cm= st.number_input("forehead_width_cm")
forehead_height_cm= st.number_input("forehead_height_cm")
nose_wide= st.number_input("nose_wide")
nose_long= st.number_input("nose_long")
lips_thin= st.number_input("lips_thin")
distance_nose_to_lip_long= st.number_input("distance_nose_to_lip_long")


new_data = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
new_data = pd.DataFrame([new_data], columns=columns)
res = pipeline.predict(new_data)
press = st.button('Gender Prediction')
if press:
    st.write(f'Female or Male ? : {res[0]}')
