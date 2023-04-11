# SHELL := /bin/bash

create_pipenv:
	pip3 install pipenv==2023.3.20
	pipenv install -r requirements.txt

export_pipenv:
	pipenv requirements > requirements.txt

run_marchmallow:
	pipenv run python3 basic/json/marshmallow_demo.py

run_flask:
	gunicorn -w 4 -b 127.0.0.1:4000 --log-conf web/gunicorn_logging.conf web.flask_demo:app

run_flask_swagger:
	pipenv run python3 flask/flask_swagger_demo.py

run_pickle:
	pipenv run python3 machine_learning/sklearn/pickle_demo.py

run_joblib:
	/usr/local/miniconda/envs/sklearn_latest/bin/python3 machine_learning/sklearn/joblib_demo.py

run_onns:
	# /usr/local/miniconda/envs/sklearn_latest/bin/pip3 install skl2onnx
	# /usr/local/miniconda/envs/sklearn_latest/bin/pip3 install onnxruntime
	/usr/local/miniconda/envs/sklearn_latest/bin/python3 machine_learning/sklearn/onns_demo.py

run_plotly:
	pipenv run python3 machine_learning/jupyter_extension/plotly_demo.py

run_bokeh:
	pipenv run python3 machine_learning/jupyter_extension/bokeh_demo.py

run_args:
	python3 basic/function/arg.py

run_pyhive:
	python3 hive/pyhive_presto_local.py

run_mysql:
	python3 mysql/pymysql_demo.py

run_file:
	python3 file/file_test.py

run_config_parse:
	pipenv run python3 config/parser.py