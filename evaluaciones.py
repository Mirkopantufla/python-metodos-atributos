from pizza import Pizza

#Punto 5-A
#Imprimo los valores de los atributos de clase
print(f'''Tamaño: {Pizza.tamano}
Precio: {Pizza.precio}''')

#Punto 5-B
#Compruebo el correcto funcionamiento de la funcion validate_possible_cases()
print(Pizza.validate_possible_cases("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

#Punto 5-C
#Creo una instancia y ejecuto el metodo para crear una orden
pruebaPizza = Pizza()
pruebaPizza.create_order()

#Punto 5-D
print(f'''
    Ingredientes Vegetales: {', '.join(pruebaPizza.ingredientes["vegetales"])}
    Ingredientes Proteicos: {pruebaPizza.ingredientes["proteicos"]}
    Tipo de masa: {pruebaPizza.masa}
    ¿La Pizza es valida?: {pruebaPizza.es_valida}
''')

#Punto 5-E
print(f'{Pizza.validate_order()}')