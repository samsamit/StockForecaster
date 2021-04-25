# StockForecaster

## Setup virtual enviroment

All scripts should be run on povershell terminal

    1. Run command ``py -3 -m venv .venv`` to create virtual anviroment
    2. Run command ``.venv\scripts\activate`` to activate virtual enviroment
    3. At this point your terminal should show ##(.venv)## at the start of the command line
    4. Run command ``pip install -r requirements.txt`` to install all libraries for this project

## Install libraries

To install any libraries you should use the virtual enviroment. There you are able to use ##pip## command to install any library you want.

Before you commit anything you should run this command `pip freeze > requirements.txt` to create a reguirements file for other developers.

## Using autopep formatter on vscode

Go to vscode setting to location `python.formatting.autopep8` and add this line to the path option `${workspaceFolder}/.venv/Scripts/autopep8`
