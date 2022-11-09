from fastapi import FastAPI, Query
from pydantic import BaseModel
import Categorias


app = FastAPI()


# connection = pymysql.connect(
#   host='localhost', user='root', password='',
#   database='integracionapi', charset='utf8mb4',
#   cursorclass=pymysql.cursors.DictCursor
# )


# Categorias


@app.get("/categorias/")
def traer_categorias():
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

import os
import time
from classes.validations import Validations
validator = Validations()

def run():
    print_options()

    command = input()
    command = command.upper()

    if command == "C":
        create_product()
    elif command == "L":
        list_products()
    elif command == "M":
        update_product()
    elif command == "R":
        delete_product()
    elif command == "S":
        search_product()
    elif command == "E":
        os._exit(1)
    else:
        print("Invalid command")
        time.sleep(1)
        run()
        
def create_contact():
    print("CREATE PRODUCT")
    print('*' * 20)
    name = check_name()
    type = check_type()
    price = check_price()
    unit = check_unit()


def check_name():
    print("Insert name:")
    name = input()
    try:
        validator.validateName(name)
        return name
    except ValueError as err:
        print(err)
        check_name()


def check_type():
    print("Insert type:")
    surname = input()
    try:
        validator.validateType(type)
        return type
    except ValueError as err:
        print(err)
        check_type()


def check_price():
    print("Insert price:")
    email = input()
    try:
        validator.validatePrice(price)
        return price
    except ValueError as err:
        print(err)
        check_price()


def check_unit():
    print("Insert unit:")
    unit = input()
    try:
        validator.validateUnit(unit)
        return unit
    except ValueError as err:
        print(err)
        check_unit()

    def check_product_data(message, data_name, force = True):
    print(message)
    input_data = input()
    if notforce and not input_data:
        return
    try:
        getattr(validator, f"validate{data_name.capitalize()}")(input_data)
        return input_data
    except ValueError as err:
        print(err)
        check_product_data(message, data_name)

def create_contact():
    print("CREATE PRODUCT")
    print('*' * 20)
    name = check_product_data("Insert name:", "name")
    type = check_product_data("Insert type:", "type")
    price = check_product_data("Insert price (without hyphens or dots):" , "price")
    unit = check_product_data("Insert unit:" , "unit")

  import os
import time
from classes.validations import Validations
from classes.product import Product
from classes.dbproducts import DBProducts
validator = Validations()
db = DBProducts()

def create_contact():

    print("CREATE PRODUCT")
    print('*' * 20)
    name = check_product_data("Insert name :", "name")
    type = check_product_data("Insert type :", "type")
    price = check_product_data("Insert price:", "price")
    unit = check_product_data("Insert unit (without hyphens or dots):", "unit")

       product = Product(None, name, type, price, unit)
    if db.save_product(product):
        print(" Product inserted successfully")
    else:
        print('Error saving product")
              
import os
import time
from classes.validations import Validations
from classes.product import Product
from classes.dbproducts import DBProducts
from prettytable import PrettyTable
validator = Validations()
db = DBProducts()

After create funtion list_products.

def list_products():
    list_products = db.list_products()

    if not list_products:
        return print("There are no saved products yet")

    table = PrettyTable(db.get_schema().keys())
    for product in list_products:
        table.add_row([
            product.id_product,
            product.name,
            product.type,
            product.price,
            product.unit
        ])

    print(table)
    print("Pulse enter to exit")
    command = input()

def run():
    print_options()

    command = input()
    command = command.upper()

    if command == "C":
        create_product()
    elif command == "L":
        list_products()
    elif command == "M":
        pass
    elif command == "R":
        pass
    elif command == "S":
        pass
    elif command == "E":
        os._exit(1)
    else:
        print("Invalid Command")

    time.sleep(1)
    run()

def search_product():

    filters = {}
    print("Enter  name (space to use other filter ):")
    nombre = input()
    if nombre:
        filters["NAME"] = nombre
    print("Enter  fullName (space to use other filter ):')
    apellidos = input()
    if apellidos:
        filters["TYPE] = tipos
    print("Enter  a typ (space to use other filter):')
    email = input()
    if email:
        filters["PRICE"] = precio

    try:
        list_products = db.search_products(filters)
        if not list_products:
            return print(" There are NOT product whit this attributes ")

        _print_table_products(list_products)
    except ValueError as err:
        print(err)
        time.sleep(1)
        search_product()


def _print_table_products(list_products):
    table = PrettyTable(db.get_schema().keys())
    for prodcut in list_products:
        table.add_row([
            product.id_product,
            product.name,
            product.type,
            product.price,
            product.unit
        ])

    print(table)
    print("Pulse one letter to continue")
    command = input()

    
def update_product():

    list_products()

    print("Enter  contact id to actualice :")
    id_object = input()

    data = {}
    nombre = check_product_data("Enter e  name (empty to keep actual name):", "name", False)
    if nombre:
        data["NAME"] = nombre
    tipo = check_product_data("Enter e a type (empty to keep actual type):", "type", False)
    if apellidos:
        data["TYPE"] = tipos
    price = check_product_data("Enter  a number (empty to keep actual price ):", "price", False)
    if email:
        data["PRICE"] = price
    unit = check_product_data("Enter a number (empty to keep actual unidad):", "unit", False)
    if unit:
        data["UNIT"] = unidad
    
    try:
        res = db.update(id_object, data)
        if res:
            print("Updated product successfully")
    except Exception as err:
        print(err)
        time.sleep(1)
        update_product()


def delete_product():
    list_products()

    print("Enter the id of the product you want to delete:")
    id_object = input()
    try:
        res = db.delete(id_object)
        if res:
            print("Product delete  successfully")
    except Exception as err:
        print(err)
        time.sleep(1)
        delete_product()

        
