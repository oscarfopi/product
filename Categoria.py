from pydantic import BaseModel


class Categoria(BaseModel):
  Id: int
  Codigo: str
  Descripcion: str
  Activo: bool

