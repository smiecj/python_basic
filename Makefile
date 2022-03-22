# SHELL := /bin/bash

create_pipenv:
	pip3 install pipenv
	pipenv install -r requirements.txt

export_pipenv:
	pipenv lock -r > requirements.txt

run_marchmallow:
	pipenv run python3 basic/json/marshmallow_demo.py

run_flask:
	pipenv run python3 flask/flask_swagger_demo.py

run_pickle:
	pipenv run python3 machine_learning/sklearn/pickle_demo.py

run_joblib:
	/usr/local/miniconda/envs/sklearn_latest/bin/python3 machine_learning/sklearn/joblib_demo.py

run_onns:
	# /usr/local/miniconda/envs/sklearn_latest/bin/pip3 install skl2onnx
	# /usr/local/miniconda/envs/sklearn_latest/bin/pip3 install onnxruntime
	/usr/local/miniconda/envs/sklearn_latest/bin/python3 machine_learning/sklearn/onns_demo.py