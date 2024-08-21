import sqlite3
conn = sqlite3.connect("ferretaria.bd")
cursor = conn.cursor()

class producto:
    def __init__(self,nombres,precios):
        self.nombres = nombres
        self.precios = precios
        cursor.execute("""CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY,nombre TEXT, precio TEXT,cantidad_prod TEXT)""")
    def insertar_productos(self,cantidad_prod):
        instruccion = f"INSERT INTO productos(nombre,precio,cantidad_prod) VALUES('{self.nombres}','{self.precios}','{cantidad_prod}')"
        cursor.execute(instruccion)
        conn.commit()
    def leer_productos(self):
        cursor.execute("SELECT * FROM productos WHERE nombre like ?",(self.nombres,))
        print(cursor.fetchall())
        conn.commit()
    def actualizar_productos(self):
        instruccion = f"UPDATE productos SET precio = ? WHERE nombre = ?",(self.precio,self.nombres)
        cursor.execute(instruccion)
    def eliminar_productos(self):
        cursor.execute("DELETE FROM productos WHERE id = ?",(self.nombres,))
        print("el dato a sido eliminado ")
        conn.commit()
    def close_bd(self):
        conn.commit()
        conn.close()







    
        
            


            