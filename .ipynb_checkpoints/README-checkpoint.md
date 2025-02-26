Create venv:
    python3 -m venv .myvenv
Enter in venv (inside project directory)
    source health_venv/bin/activate

Deactivate
    deactivate

## Install the deps

pip install langchain
pip install jupyterlab


pip install django openai requests django-cors-headers

## Start a django project named "chatbot" containing the base structure of a Django project.

django-admin startproject chatbot 

cd chatbot

## Create a new app named "health_counseller" withing djang project
python manage.py startapp health_counseller



## How to run the project

    #1 Migrate the models
        python manage.py migrate  # for migrating modified model changes to database

    #2 Run local server
        python manage.py runserver or python manage.py runserver 8080



# project -> https://www.youtube.com/watch?v=MoqgmWV1fm8
# pip install jupyterlab ? for interacive interface in ide

## How to launch JupyterLab with:
jupyter lab


## How to launch Jupyter notebook with:
jupyter notebook