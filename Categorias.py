import Conexion


def traer_categorias():
  with Conexion.connection:
    with Conexion.connection.cursor() as cursor:
      sql = "SELECT * FROM Categorias"
      cursor.execute(sql)
      result = cursor.fetchone()
      return result

