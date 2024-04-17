import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier

#loading up the Classification model we created

model = DecisionTreeClassifier(criterion='entropy', max_depth=10, min_samples_leaf=5,
                       random_state=0)
model = joblib.load('finalized_model.joblib')

def prediction(Buying, Maint, Doors, Persons, Lug_boot, safety):
  if Safety == 'med':
    Safety = 1
  elif Safety == 'high':
    Safety = 2
  elif Safety == 'low':
    Safety = 3
  df = pd.DataFrame([Buying, Maint, Doors, Persons, Lug_boot, safety],columns=[Buying, Maint, Doors, Persons, Lug_boot, safety])
  preduction = model.predict([Buying, Maint, Doors, Persons, Lug_boot, safety])
  return result
st.title('bike Evaluation Classification')
st.image("""https://upload.wikimedia.org/wikipedia/commons/0/04/RD-350.jpg""")
st.header('Enter information of the bike')
st.text("vhigh = 1 high = 2 med =3 low = 4")
Buying = st.number_input('Buying','min_values=1','max_values=4''values=1')
st.text("vhigh = 1 high = 2 med 3 low = 4")
Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)
st.text("2-Doors = 1 3-Doors 2 4-Doors = 3 5more = 4")
Doors=st.number_input('doors:', min_value=1, max_value=4, value=1)
st.text("2-persons = 1 4-persons = 2 more = 3 ")
Persons = st.number_input('persons:', min_value=1, max_value=3, value=1)
st.text("small 1 med 2 big = 3")
Lug_boot = st.number_input('lug_boot:', min_value=1, max_value=3, value=1)
Safety = st.radio('safety:', ('med', 'high', 'low'))  
if st.button('submit_car_Infos'):
  cal_eval = predict(Buying, Maint, Doors, Persons, Lug_boot, safety)
  st.success(f'The Evaluation of bike : {cal_eval[0]}')
