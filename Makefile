.PHONY : lint format sort start migrations migrate install

lint:
	flake8 .

format:
	black .

sort:
	isort .

start:
	python ./src/manage.py runserver

shell:
	python ./src/manage.py shell

migrations:
	python ./src/manage.py makemigrations

migrate:
	python ./src/manage.py migrate

install:
	pip install -r requirements.txt
