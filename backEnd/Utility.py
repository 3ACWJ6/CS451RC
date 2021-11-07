# Import <
from os import path
from json import load
from dash import Dash

# >


# Declaration <
application = Dash(suppress_callback_exceptions = True)
server = application.server

# >


def getJSON(file: str) -> dict:
    '''  '''

    directory = '/'.join(path.realpath(__file__).split('/')[:-2])
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)
