import os
import requests
import streamlit as st
import math
import numpy as np
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

def predict_class(project: str,endpoint_id: str,instances,
location: str = "us-central1",api_endpoint: str = "{region}-aiplatform.googleapis.com"):

    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

    instances_dict = [instances]

    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )

    response = client.predict(
        endpoint=endpoint, instances=instances_dict
    )
    print("deployed_model_id:", response.deployed_model_id)
    
    if response.predictions[0] == 0:
        st.success("You are not diabetic")
    else:
        st.error("You are diabetic")


st.title("Welcome to Diabetes Prediction App")
st.header("Please enter the following details:")

preg = st.number_input('Number of pregnancies:')
gluc = st.number_input('Glucose level:')
bp = st.number_input('Blood pressure:')
sth = st.number_input('Skin thickness:')
insu = st.number_input('Insulin level:')
bmi = st.number_input('BMI:')
dpf = st.number_input('Diabetes pedigree function:')
age = st.number_input('Age:')

if st.button("Predict"):

    predict_class(
    project="ENTER YOUR DETAILS",
    endpoint_id="ENTER YOUR DETAILS",
    location="ENTER YOUR DETAILS",
    instances=[preg,gluc,bp,sth,insu,bmi, dpf,age])
