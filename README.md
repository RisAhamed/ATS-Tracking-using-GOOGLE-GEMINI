# ATS-Tracking-using-GOOGLE-GEMINI


# project structure
```bash 
ats-project/
├── data/
│   ├── job_postings.csv
│   ├── candidate_applications.csv
│   ├── resumes/
│   │   ├── resume1.pdf
│   │   ├── resume2.pdf
│   │   └── ...
│   └── ...
├── models/
│   ├── candidate_matching_model.pkl
│   ├── ranking_model.pkl
│   └── ...
├── code/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── data_processing.py
│   ├── utils.py
│   └── ...
├── configs/
│   ├── environment_variables.py
│   ├── model_configs.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_models.py
│   └── ...
├── mlops/
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── train_pipeline.py
│   │   └── ...
│   ├── workflows/
│   │   ├── __init__.py
│   │   ├── train_workflow.py
│   │   └── ...
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── model_monitoring.py
│   │   └── ...
│   └── ...
├── logs/
│   ├── project.log
│   └── ...
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

# required libraries

``` bash 
scikit-learn
tensorflow
pandas
numpy
scipy
mlflow
kubeflow
apache-beam
google-cloud-aiplatform
flask
sqlalchemy
docker
gitpython
boto3
```

install the libraries using the following command 
``` bash 
pip install -r requirements.txt
```