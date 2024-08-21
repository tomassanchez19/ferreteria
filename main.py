from productos import producto
from provedores import provedor
i = 1
tablas = str(input("Ingrese el nombre de la tabla con la que quiere interactuar: "))
while i>=1:
    parametro1 = 0
    parametro2 = 0
    if tablas == "productos":
        print("                TABLA PRODUCTOS                                 ")
        res_siono = "si"
        respuesta = str(input("Que operacion quiere hacer: "))
        if respuesta == "insertar":
            while res_siono== "si":
                parametro1 = input("Ingrese nombre del producto: ")
                parametro2 = input("Ingrese precio de " + parametro1 + ": ")
                parametro3 = input("ingrese a cantidad de "+ parametro1 + "dsiponible: ")
                prod = producto(parametro1,parametro2)
                prod.insertar_productos(parametro3)
                res_siono = input("quiere seguir ingresando productos: ")
        elif respuesta == "leer":
            while res_siono == "si":
                parametro1 = input("Ingrese nombre del producto que quiera leer: ")
                prod = producto(parametro1,parametro2)
                prod.leer_productos()
                res_siono = input("quiere seguir leyendo productos: ")

        elif respuesta == "actualizar":
            while res_siono == "si":
                parametro1 = input("Ingrese nombre del producto que vas a actualizar: ")
                parametro2 = input("ingrese el nuevo valor del preducto: ")
                prod = producto(parametro1,parametro2)
                prod.actualizar_productos()
                res_siono = input("quieres actualizar algun otro producto: ")
        elif respuesta == "eliminar":
            while res_siono == "si":
                parametro1 = int(input("Ingrese el id del producto que quiera eliminar: "))
                prod = producto(parametro1,parametro2)
                prod.eliminar_productos()
                res_siono = input("quiere seguir eliminando productos: ")
        elif respuesta == "salida":
            print("                TABLA PRODUCTOS CERRADA                ")
            prod = producto(parametro1, parametro2)
            prod.close_bd()
            tablas = ""
        else:
            print("error: ingrese correctamente la operacion ")

    elif tablas == "provedores":
        print("                TABLA PROVEDORES                                 ")
        res_siono = "si"
        respuesta = str(input("Que operacion quiere hacer: "))
        if respuesta == "insertar":
            while res_siono== "si":
                parametro1 = input("Ingrese nombre del provedor: ")
                parametro2 = input("Ingrese productos que vende " + parametro1 + ": ")
                prov = provedor(parametro1,parametro2)
                prov.insertar_provedores()
                res_siono = input("quiere seguir ingresando provedores: ")
        elif respuesta == "leer":
            while res_siono == "si":
                parametro1 = input("Ingrese nombre del provedor que quiera ver: ")
                prov = provedor(parametro1,parametro2)
                prov.leer_provedores()
                res_siono = input("quiere seguir viendo provedores: ")

        elif respuesta == "actualizar":
            while res_siono == "si":
                parametro1 = input("Ingrese nombre del provedor que vas a actualizar: ")
                parametro2 = input("ingrese el nuevo valor del provedor: ")
                prov = provedor(parametro1,parametro2)
                prov.actualizar_provedores()
                res_siono = input("quieres actualizar algun otro provedor: ")
        elif respuesta == "eliminar":
            while res_siono == "si":
                parametro1 = int(input("Ingrese nombre del provedor que quiera eliminar: "))
                prov = provedor(parametro1,parametro2)
                prov.eliminar_provedores()
                res_siono = input("quiere seguir eliminando provedores: ")
        elif respuesta == "salida":
            print("           TABLA PROVEDORES CERRADA                ")
            prov = provedor(parametro1,parametro2)
            prov.close_bd()
            tablas = ""
        else:
            print("error: ingrese correctamente la operacion ")


