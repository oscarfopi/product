import Categorias

from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


# Categorias


@app.get("/categorias/")
async def traer_categorias():
  # codigo para leer de DB y crear objeto para mostrar
  return Categorias.traer_categorias()


# Productos


@app.get("/productos/")
async def traer_productos():
  # codigo para leer de DB y crear objeto para mostrar
  return "productos"


# Proveedores


@app.get("/proveedores/")
async def traer_proveedores():
  # codigo para leer de DB y crear objeto para mostrar
  return "proveedores"


# Compras


@app.get("/compras/")
async def traer_compras():
  # codigo para leer de DB y crear objeto para mostrar
  return "compras"


# Facturas


@app.get("/facturas/")
async def traer_facturas():
  # codigo para leer de DB y crear objeto para mostrar
  return "facturas"


