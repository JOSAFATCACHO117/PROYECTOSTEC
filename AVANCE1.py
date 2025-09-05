#Hola compañero programador! Sé bienvenido a mi código de máquinas expendedoras 
#con temática variable. Mi proyecto tendrá varios diccionarios, por ejemplo, este que se presenta por aquí es el catálogo de gym, posterioemente habrá un catálogo
#de biblioteca, zonas comunes, salones y demás!. Ya sin perder tanto el tiempo, ¿comenzamos? :)#

catalogo_gym ={ 
                "A1" : ("MonsterTec", 30),
                "A2" : ("EnergyTec" , 25),
                "A3" : ("HydroTec", 15),
                "A4" : ("Barra Proteica Chocotec", 28),
                "A5" : ("Barra proteinca VaniTec", 28),
                "A6" : ("Agua Mineral TecFresh", 12),
                "A7" : ("Agua Natrual PureTec", 10),
                "A8" : ("Jugo de Naranja PoweFit", 20),
                "A9" : ("Bebida isotónica IonTec", 22),
                "A10" : ("Papas Fit Jalpaeño ", 18),
                "A11" : ("Papas Fir Limón", 18),
                "A12" : ("Mix de nueces NutriTec", 35),
                "A13" : ("Galletas de Avena", 16),
                "A14" : ("Cholate Amargo", 24),
                "A15" : ("Smoothie Proteíco", 50),
            }
print("Bienvenido usuario, seleccione el producto deseado")
producto = input()
if producto == "A1":
    print(catalogo_gym["A1"]) 
    print("¿Cuántas unidades?")
    unidades = int(input())
    costo = catalogo_gym["A1"][1]
    precio_final = costo * unidades
    print(precio_final, " mxn")
    print("Introduzca su monto")
    dinero_cliente = float(input())
    
    def cambio_cliente(x):
        cambio = dinero_cliente - (catalogo_gym["A1"][1]*unidades)
        return cambio
    
print(cambio_cliente(dinero_cliente), " pesos de cambio")  

# de momento es todo :), estoy intendo buscar una función que me ayude
# a no meter tantas líneas y poder condensarlo. Por ejemplo, tal vez meter
# todo el proceso de selección y pago dentro de una función, para sí
# simplemente llamarla. Espero que nos veamos pronto!!!! #
