# Diabetes Predicor GCP Deployment Walkthrough

By using Vertex AI by GCP one can deploy models easily that are trained by frameworks like scikit-learn, pytorch, tensorflow and xgboost.

## Information about Dataset and Model
Dataset taken from Kaggle: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database<br>
Model taken from running notebook: https://www.kaggle.com/code/rishpande/pima-indians-diabetes-beginner

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
* In model settings section choose the framework, its version and pickled model location.
* If you want explainability you can choose it or skip.
* Finally click the import button.
