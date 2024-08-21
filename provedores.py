import sqlite3
conn = sqlite3.connect("ferretaria.bd")
cursor = conn.cursor()
class provedor:
    def __init__(self,nombres_prov,productos_prov):
        self.nombres_prov = nombres_prov
        self.productos_prov = productos_prov
        cursor.execute("""CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY,nombre TEXT, producto TEXT)""")
    def insertar_provedores(self):
        instruccion = f"INSERT INTO provedores(nombre,producto) VALUES('{self.nombres_prov}','{self.productos_prov}')"
        cursor.execute(instruccion)
        conn.commit()
    def leer_provedores(self):
        cursor.execute("SELECT * FROM provedores WHERE nombre like ?",(self.nombres_prov,))
        print(cursor.fetchall())
        conn.commit()
    def actualizar_provedores(self):
        cursor.execute("UPDATE provedores SET producto = ? WHERE nombre = ?",(self.productos_prov,self.nombres_prov))
    def eliminar_provedores(self):
        cursor.execute("DELETE FROM productos WHERE id = ?",(self.nombres_prov,))
        print("el dato a sido eliminado ")
        conn.commit()
    def close_bd(self):
        conn.commit()
        conn.close()