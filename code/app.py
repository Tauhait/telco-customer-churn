import streamlit as st
from PIL import Image
import requests
import pandas as pd
import json

host = 'churn-serving-env.eba-qim2wdpe.ap-south-1.elasticbeanstalk.com'
url = 'http://%s/predict' % host

def run_app():
    #Setting Application title
    st.title('Telco Customer Churn Prediction App')

      #Setting Application description
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn in a ficitional telecommunication use case.
    The application is functional for both online prediction and batch data prediction. n
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    image = Image.open('../imgs/customer-churn-app-img.png')
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?", ("Online", "Batch"))
    st.sidebar.info('This app is created to predict Customer Churn')
    st.sidebar.image(image)
    if add_selectbox == "Online":
        st.info("Input data below")
        #Based on our optimal features selection
        st.subheader("Demographic data")
        gender = st.selectbox('Gender:', ('male', 'female'))
        partner = st.selectbox('Partner:', ('yes', 'no'))
        seniorcitizen = st.selectbox('Senior Citizen:', ('yes', 'no'))
        dependents = st.selectbox('Dependent:', ('yes', 'no'))
        
        st.subheader("Payment data")
        tenure = st.slider('Number of months the customer has stayed with the company', min_value=0, max_value=72, value=0)
        contract = st.selectbox('Contract', ('month-to-month', 'one_year', 'two_year'))
        paperlessbilling = st.selectbox('Paperless Billing', ('yes', 'no'))
        paymentmethod = st.selectbox('PaymentMethod',('electronic_check', 'mailed_check', 'bank_transfer_(automatic)','credit_card_(automatic)'))
        monthlycharges = st.number_input('The amount charged to the customer monthly', min_value=0, max_value=150, value=0)
        totalcharges = st.number_input('The total amount charged to the customer',min_value=0, max_value=10000, value=0)

        st.subheader("Services signed up for")
        mutliplelines = st.selectbox("Does the customer have multiple lines",('yes','no','no_phone-service'))
        phoneservice = st.selectbox('Phone Service:', ('yes', 'no'))
        internetservice = st.selectbox("Does the customer have internet service", ('dsl', 'fiber_optic', 'no'))
        onlinesecurity = st.selectbox("Does the customer have online security",('yes','no','no_internet_service'))
        deviceprotection = st.selectbox("Does the customer have device protection",('yes','no','no_internet_service'))
        onlinebackup = st.selectbox("Does the customer have online backup",('yes','no','no_internet_service'))
        techsupport = st.selectbox("Does the customer have technology support", ('yes','no','no_internet_service'))
        streamingtv = st.selectbox("Does the customer stream TV", ('yes','no','no_internet_service'))
        streamingmovies = st.selectbox("Does the customer stream movies", ('yes','no','no_internet_service'))
        
        data = {
            'customerid': '8879-zkjof',
            'gender': gender,
            'seniorcitizen': seniorcitizen,
            'partner': partner,
            'dependents': dependents,
            'tenure':tenure,
            'phoneservice': phoneservice,
            'multiplelines': mutliplelines,
            'internetservice': internetservice,
            'onlinesecurity': onlinesecurity,
            'onlinebackup': onlinebackup,
            'deviceprotection': deviceprotection,
            'techsupport': techsupport,
            'streamingtv': streamingtv,
            'streamingmovies': streamingmovies,
            'contract': contract,
            'paperlessbilling': paperlessbilling,
            'paymentmethod': paymentmethod,
            'monthlycharges': monthlycharges,
            'totalcharges': totalcharges
        }
        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.write('Overview of input is shown below')
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.dataframe(features_df)
    else:
        st.subheader("Dataset upload")
        file = st.file_uploader("Choose a file")
        if file is not None:
            # Read the uploaded file as bytes
            data_bytes = file.read()

            # Convert the bytes data to a string (assuming it is in UTF-8 encoding)
            data_str = data_bytes.decode("utf-8")

            # Deserialize the string to a Python dictionary
            data = json.loads(data_str)
            # df = pd.DataFrame.from_dict(data)
            #Get overview of data
            st.write(data)
            st.markdown("<h3></h3>", unsafe_allow_html=True)
    
    if st.button('Predict'):
        response = requests.post(url, json=data)
        result = response.json()
        st.write(result)
        if result['churn'] == True:
            st.warning('Yes, the customer will terminate the service.')
        else:
            st.success('No, the customer is happy with Telco Services.')

if __name__ == '__main__':
    run_app()