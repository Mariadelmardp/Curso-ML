import psycopg2
import pandas as pd

def conexion_Chinook(sql_query):
  conn = psycopg2.connect (host = "localhost", 
                        database = "Chinook",
                        user = "postgres", 
                        password = "9366")
  cursor = conn.cursor() 
  cursor.execute(sql_query) 
  rows = cursor.fetchall() 
  tabla = pd.DataFrame(rows)
  colnames = [desc[0] for desc in cursor.description] 
  tabla = tabla.set_axis(colnames, axis = 1)
  cursor.close()
  conn.close()

  return tabla