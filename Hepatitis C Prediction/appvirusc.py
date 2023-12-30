import streamlit as st
import joblib


model = joblib.load('rf_best_model.pkl')



def preprocess_input(value):

    
    try:
        value = float(value)
    except ValueError:
        value = None
    return value

def predict_category(features):
    prediction = model.predict(features)
    return prediction[0]


def main():
    st.title('Hepatitis C Prediction App')

   
    age = st.number_input('Age', 0)
    
    
    sex_options = ['Male', 'Female']
    sex = st.selectbox('Sex', sex_options)

    alb = preprocess_input(st.text_input('Albumin Blood Test (ALB) g/L', '0'))
    alp = preprocess_input(st.text_input('Alkaline Phosphatase Test (ALP) IU/L', '0'))
    alt = preprocess_input(st.text_input('Alanine Transaminase Test (ALT) U/L', '0'))
    ast = preprocess_input(st.text_input('Aspartate Transaminase Test (AST) U/L', '0'))
    bil = preprocess_input(st.text_input('Bilirubin Blood Test (BIL) µmol/L', '0'))
    che = preprocess_input(st.text_input('Cholinesterase (CHE) kU/L', '0'))
    chol = preprocess_input(st.text_input('Cholesterol (CHOL) mmol/L', '0'))
    crea = preprocess_input(st.text_input('Creatinine Blod Test (CREA) µmol/L', '0'))
    ggt = preprocess_input(st.text_input('Gamma-Glutamyl Transpeptidase Test (GGT) U/L', 0))
    prot = preprocess_input(st.text_input('Protein Blood Test (PROT) g/L', '0'))

    
    sex = 1 if sex == 'Male' else 0

    
    features = [[age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]]

    
    if st.button('Predict'):
        prediction = predict_category(features)
        if prediction == 1:
            st.success('The Person Is Infected.')
        else:
            st.success('The Person Is Not Infected.')

if __name__ == '__main__':
    main()
