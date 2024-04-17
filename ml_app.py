import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier

#loding up the classification model we created
model = DecisionTreeClassifier(max_depth=20, min_samples_leaf=5, random_state=0)
model = joblib.load('finalized_model.joblib')

#caching the model for faster loading
@st.cache

#Define the prediction function

def prediction(Buying,Maint,Doors,Persons,Lug_boots,Safety):
  if Safety == 'med':
    safety = 1
  elif Safety == 'high':
    safety = 2
  elif Safety == 'low':
    safety = 3
  df = pd.DataFrame([[Buying,Maint,Doors,Persons,Lug_boots,safety]],
                    columns=['Buying','Maint','Doors','Persons','Lug_boots','safety'])
  result=model.predict([[Buying,Maint,Doors,Persons,Lug_boots,safety]])
  return result

st.title('car evaluation Classification')
st.image("""https://www.google.com/imgres?imgurl=https%3A%2F%2Fimgd.aeplcdn.com%2F664x374%2Fn%2Fcw%2Fec%2F27074%2Fcivic-exterior-rear-view.jpeg%3Fq%3D80&tbnid=dB-g86tAcTgPlM&vet=12ahUKEwi2v9uH4MiFAxW4tGMGHdq8BdEQMygBegQIARAz..i&imgrefurl=https%3A%2F%2Fwww.carwale.com%2Fhonda-cars%2Fcivic%2F&docid=Nd62i21YXmSxaM&w=664&h=374&q=civic%20honda&ved=2ahUKEwi2v9uH4MiFAxW4tGMGHdq8BdEQMygBegQIARAz""")
st.header('Enter the Information of the Car:')
st.text("vigh = 1 high = 2 med = 3 low = 4")
Buying = st.number_input('buying:',min_value = 1,max_value = 4,value=1)
st.text("vigh = 1 high = 2 med = 3 low = 4")
Maint = st.number_input('maint:',min_value = 1,max_value = 4,value=1)
st.text("2-Doors = 1 3-Doors = 2 4-Doors = 3 5more = 4")
Doors = st.number_input('doors:',min_value = 1,max_value = 4,value=1)
st.text("2-Persons = 1 4-Persons = 2 more = 3")
Persons= st.number_input('Persons:',min_value = 1,max_value = 4,value=1)
st.text("small = 1 med = 2 big = 3")
Lug_boot= st.number_input('lug_boot:',min_value = 1,max_value = 4,value=1)
Safety = st.radio('safety:',('med','high','low'))

if st.button('Submit_Cars_Infos'):
  cal_eval = prediction(Buying,Maint,Doors,Persons,Lug_boot,Safety)
  st.success(f'The Evaluation of Car : {cal_eval[0]}')
