# Importar FastApi
from fastapi import FastApi, Query
from fastapi.responses import HTMLResponse

# Importar el archivo .py de las funciones que se ejecutaran en la API
import funciones as f
import importlib

importlib.reload(f)
