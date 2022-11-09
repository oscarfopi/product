class product:

    def __init__(self, name, type, price,  unit):
        self._name = name
        self._type = type
        self._price = price
        self._unit = unit

@property
def name(self):
    return self._name

@name.setter
def name(self, name):
    self._name = name

@property
def type(self):
    return self._type

@surname.setter
def type(self, type):
    self._type = type

@property
def price(self):
    return self._price

@email.setter
def price(self, price):
    self._price = price

@property
def unit(self):
    return self._unit

@phone.setter
def unit(self, unit):
    self._unit = unit

class Product:

    def __init__(self, id_product, name, type, price, unit):
        self._id_product = id_product
        self._name = name
        self._type = type
        self._price = price
        self._unit = unit
        
    @property
    def id_product(self):
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        self._id_product = id_product

    .
    .
    .

def save_contact(self, product):
        data = [product.name, produc.type, product.price, product.unit]
        return self.insert(data)
    


 def list_products(self):
        list_products = self.get_all()

        if not list_products:
            return None

        object_products = []
        # Convert the data to objects of type product
        for product in list_productts:
            c = Product(product['ID'], product["NAME"], product["TYPE"], product["PRICE"], product["UNIT"])
            object_products.append(c)

        return object_products
    
    
    def get_schema(self):
        return SCHEMA


 def delete_product(self, id_object):
        if not id_object:
            raise ValueError("Must send contac id")
        self.delete(id_object)



        
    

                           
