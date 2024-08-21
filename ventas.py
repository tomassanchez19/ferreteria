import sqlite3
conn = sqlite3.connect("ferretaria.bd")
cursor = conn.cursor()
class venta:
    def __init__(self,fecha_venta,nombre_prod,monto_total):
        self.fecha_venta = fecha_venta
        self.nombre_prod = nombre_prod
        self.monto_total = monto_total 
        cursor.execute("""CREATE TABLE IF NOT EXISTS ventas (id INTRGER PRIMARY KEY, fecha_venta TEXT ,nombre_prod TEXT,cantidad_prod TEXT, monto_total TEXT)""")
    def insertar_ventas(self):
        instruccion = f"INSERT INTO ventas(fecha_venta,nombre_prod,cantidad_prod,monto_total)VALUES('{self.fecha_venta}','{self.nombre_prod}','{self.cantidad_prod}','{self.monto_total}')"
        cursor.execute(instruccion)
        
