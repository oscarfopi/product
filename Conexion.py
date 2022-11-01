import pymysql.cursors


connection = pymysql.connect(
  host='localhost', user='root', password='',
  database='integracionapi', charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)