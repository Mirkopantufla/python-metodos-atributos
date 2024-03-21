from ingredientes import meat_ingredients, vegetable_ingredients, dough_type

#Punto 1
#Creo la clase con sus atributos de clase
class Pizza():
    precio = 10000
    tamano = "familiar"

    #Constructor para inicializar los valores atribuibles (no requerido pero evito errores de ejecución)
    def __init__(self):
        self.ingredientes = {
        "proteicos": "",
        "vegetales": []
        }
        self.masa = ""
        self.es_valida = False
    
    #Punto 2
    #Funcion estatica 
    @staticmethod
    def validate_possible_cases(text:str, ingredientList:list):
        return True if text in ingredientList else False

    #Punto 3
    #Funcion para crear las ordenes
    def create_order(self):
        #Asigno a cada atributo lo ingresado por el usuario
        self.ingredientes["proteicos"] = input(f'''
        Ingrese uno de los siguientes ingredientes proteicos:
            [ {" | ".join(meat_ingredients)} ]

        > ''')

        self.ingredientes["vegetales"].append(input(f'''
        Ingrese el primer ingrediente vegetal:
            [ {" | ".join(vegetable_ingredients)} ]
        > '''))

        self.ingredientes["vegetales"].append(input(f'''
        Ingrese el segundo ingrediente vegetal:
            [ {" | ".join(vegetable_ingredients)} ]
        > '''))

        self.masa = input(f'''
        Ingrese uno una de los siguientes tipos de masa:
            [ {" | ".join(dough_type)} ]
        > ''')

        #Ejecuto funcion del punto 4
        self.validate_order()

    #Punto 4
    #Funcion para validar lo ingresado por el usuario
    def validate_order(self):
        #Asigno a variables cada dato requerido para la validacion (recuerdo haber escuchado que era recomendado hacerlo)
        ingProteico = self.ingredientes["proteicos"]
        primerIngVegetal = self.ingredientes["vegetales"][0]
        segundoIngVegetal = self.ingredientes["vegetales"][1]
        tipoMasa = self.masa

        #Ejecuto la funcion del punto dos para cada ingrediente, asi obtengo si son validos para caso
        validateMeat = self.validate_possible_cases(ingProteico, meat_ingredients)
        validateFirstVegetable = self.validate_possible_cases(primerIngVegetal, vegetable_ingredients)
        validateSecondVegetable = self.validate_possible_cases(segundoIngVegetal, vegetable_ingredients)
        validateDoughType = self.validate_possible_cases(tipoMasa, dough_type)

        #Evaluo si todos los ingredientes fueron ingresados correctamente y asigno a atributo el resultado.
        if validateMeat and validateFirstVegetable and validateSecondVegetable and validateDoughType:
            self.es_valida = True
        else:
            self.es_valida = False