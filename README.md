# python-gradient-abstracts
Abstract artistic background images created with code

## Research
- Create a vector graphic with ``python 3``
- Descided for ``<svg>`` as a output format
- Descided not to use any imported library

# Create my setup
## Visual Studio Code Community edition
- I choose to work in Visual Studio Code Community edition
- First I open a terminal and navigate into the my documents
- I git clone the repository and open it in VS Code
- - ``git clone git@github.com:matthias-jaeger-net/python-gradient-abstracts.git``
- Then I open a new terminal and proceeed with the setup

## Python 3 virtualenv
- Create a new directory to 'rest' the virtualenv
- - ```mkdir venv```
- Installing the virtualenv in the directory
- - ```virtualenv -p python3 venv```
- Activating the virtualenv
- - ```source venv/bin/activate```
- Hide the venv for gitHub, create a gitignore file
- - ``echo '/venv/' > .gitignore``

## Create the working directory
- mkdir work
- cd work
- touch test.py
- echo 'print("hello world")' > test.py
- python test.py
- hello world
