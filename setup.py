from setuptools import setup, find_packages

setup(
    name="ats-project",
    version="1.0.0",
    author="RisAhamed",
    author_email="riswanahamed38@gmail.com",
    description="Application Tracking System (ATS) project",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "tensorflow",
        "pandas",
        "numpy",
        "scipy",
        "mlflow",
        "kubeflow",
        "apache-beam",
        "google-cloud-aiplatform",
        "flask",
        "sqlalchemy",
        "docker",
        "gitpython",
        "boto3"
    ]
)