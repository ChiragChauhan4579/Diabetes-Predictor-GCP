# Diabetes Predictor GCP Deployment Walkthrough

By using Vertex AI by GCP one can deploy models easily that are trained by frameworks like scikit-learn, pytorch, tensorflow and xgboost.

## Information about Dataset and Model
Dataset taken from Kaggle: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database<br>

The GradientBoost model in pickle format is available in the repo so you can just clone the repo to get started.

```
git clone https://github.com/ChiragChauhan4579/Diabetes-Predicor-GCP
```

To install required libraries run this command

```
pip install -r requirements.txt
```

## GCP API creation

Lets start by storing the models pickled file on cloud storage. To do this search for `Cloud Storage` on GCP console and then create a bucket there with your required configurations. After createing the bucket you can see various upload options so upload your pkl file through that.

## Hosting the model on Vertex AI platform

* Search `Vertex AI` and go to the model registry through the left hand pane in the there. Click on `Import` button to start registering a new model by giving it a name.
* In model settings section choose the `framework, its version (here the version is 0.20) and pickled model location`.
* If you want explainability you can choose it or skip.
* Finally click the `import button`. Model import will take some time.
* Create the endpoint of that model by going to endpoint section in left pane.

**Note**: Your model name should be strictly `model.pkl`

## gcloud cli install and setup

* Install the cli using this [link](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to)
* Create the credential file as mentioned in instructions using `gcloud auth application-default login`

## Streamlit app

Run the application after changing the file as

* Give the `endpoint deployed region` in predict_class argument api_endpoint.
* Input your details when calling predict_class function by going to sample request -> python in created endpoint of vertex ai.<br>
  predict_class(
    project="ENTER YOUR DETAILS",
    endpoint_id="ENTER YOUR DETAILS",
    location="ENTER YOUR DETAILS",
    instances=[preg,gluc,bp,sth,insu,bmi, dpf,age])

```
streamlit run app.py
```

Output:

![output](https://github.com/ChiragChauhan4579/Diabetes-Predictor-GCP/blob/main/output.PNG)
