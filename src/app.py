############################# Streamlit ##############################

from pickle import load
import streamlit as st

class_dict = {
    "0": "No Sobrevive",
    "1": "Sobrevive",
}

model = load(open("../models/model_t_42.sav", "rb"))

st.title("Iris - Model prediction")

val1 = st.slider("Pclass:", min_value = 1.0, max_value = 3.0, step = 1)
val2 = st.slider("Fare:", min_value = 0.0, max_value = 550.0, step = 1)

val3 = st.slider("Sex: M(0), F(1)", min_value = 0, max_value = 1, step = 1)

val4 = st.slider("Embarked:", min_value = 0, max_value = 2, step = 1)
val5 = st.slider("FamMenbers:", min_value = 0, max_value = 10, step = 1)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4,val5]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)