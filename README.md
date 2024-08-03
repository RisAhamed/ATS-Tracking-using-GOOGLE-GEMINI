# ATS-Tracking-using-GOOGLE-GEMINI


#project structure
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
│   ├── app.py
│   ├── models.py
│   ├── data_processing.py
│   ├── utils.py
│   ├── train.py
│   ├── predict.py
│   └── ...
├── configs/
│   ├── environment_variables.py
│   ├── model_configs.py
│   ├── hyperparameters.yaml
│   └── ...
├── tests/
│   ├── test_app.py
│   ├── test_models.py
│   └── ...
├── mlops/
│   ├── pipelines/
│   │   ├── train_pipeline.py
│   │   ├── deploy_pipeline.py
│   │   └── ...
│   ├── workflows/
│   │   ├── train_workflow.py
│   │   ├── deploy_workflow.py
│   │   └── ...
│   ├── monitoring/
│   │   ├── model_monitoring.py
│   │   ├── data_monitoring.py
│   │   └── ...
│   └── ...
├── Dockerfile
├── requirements.txt
├── .gitignore
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