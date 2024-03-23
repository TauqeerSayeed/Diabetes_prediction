import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# input_data = (8,183,64,0,0,23.3,0.672,32)

# input_data = (8,183,64,0,0,23.3,0.672,32)

# input_data_as_numpy_array = np.asarray(input_data)

# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# print(input_data_reshaped)

# prediction = loaded_model.predict(input_data_reshaped)
# print(prediction)

# if(prediction[0]==0):
#   print("It is not diabetic")
# else:
#   print("it is diabetic")
  
def diabetes_prediction(input_data):
  input_data_as_numpy_array = np.asarray(input_data)  
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  # print(input_data_reshaped)

  prediction = loaded_model.predict(input_data_reshaped)
  print(prediction)
  print(input_data)

  if(prediction[0]==0):
    return 'It is not diabetic'
  else:
    return 'it is diabetic'
  
  
def main():
  
  #giving a  title
  st.title('Diabetes Prediction Web App')
  
  #getting the input data from user
  
  #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
  Pregnancies = st.text_input('No.of Pregnancies')
  Glucose = st.text_input('Glucose Level')
  BloodPressure = st.text_input('BloodPressure Level')
  SkinThickness = st.text_input('SkinThickness Level')
  Insulin = st.text_input('Insulin Level')
  BMI = st.text_input('BMI Level')
  DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Level')
  Age = st.text_input('Age in years')
  
  #code for prediction
  diagnosis = ''
  
  #creating a button for prediction
  
  if st.button('Diabetes Test Result'):
    diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])  
    
  st.success(diagnosis)
  # print(diagnosis)
  
  footer_html = """
  <footer class="footer">
    <p>&copy; Built by Tauqeer Sayeed</p>
    <a href="https://github.com/TauqeerSayeed">Github</a>
  </footer>
  """
  st.markdown(footer_html, unsafe_allow_html=True)
  
  
if __name__ == '__main__':
  main()
  
  
  
  

  


