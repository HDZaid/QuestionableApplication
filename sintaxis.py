# estructura y sintaxis útil.


# IMPRIMIR UN MENSAJE:----------------------------------------------------------------
print('hola mundo')

#TIPOS DE VARIABLES-------------------------------------------------------------------
libro = 'LUNA DE PLUTÓN'    #TEXTO
numero = 20.12              #NUMEROS
autorizado = True           #BOOLEANOS
selecionado = False         #BOOLEANOS

listaNumeros=[1,2,3,4,5]    #LISTA DE NUERMOS
print(listaNumeros[2])      #IMPRIMIENDO EL INDICE

listaTexto = ['hola', 'mundo', 'goku']  #LISTA DE TEXTO
print(listaTexto[2])                    #IMPRIMIENDO EL INDICE

listaMixta = [1, 'vegeta', 11.2]        #IMPRIMIENDO LISTA MIXTA
print(listaMixta[1])                    #IMPRIMIENDO EL INDICE

#MAPAS, OBJETOS O DICCIONARIOS:-------------------------------------------------------
personajes = {
    1: 'goku',
    2: 'vegeta',
    3: 'bulma',
    4: 'gohan'
}
print (personajes[3])

#OPERADORES ARITMETICOS ------------------------------------------------------
print('SUMA')
print(1+1) #SUMA
print('RESTA')
print(1-1) #SUMA
print('MULTIPLICACION')
print(2*2) #SUMA
print('DIVISION')
print(2/2) #SUMA

# OPERADORES COMPARATIVOS------------------------------------------------------

print(10 == 10) 

# CONDICIONALES------------------------------------------------------------------

autorizado = False

if autorizado:
    print("autorizado")
else:
    print("NO esta autorizado")
    

NumeroAutorizador = 98

if NumeroAutorizador == 100:
    print("el entero es 100")
elif NumeroAutorizador == 99:
    print("el entero es 99")
else:
    print("el entero es otro numero")
    

color = "lasdjkflk"

match color:
    case "verde":
        print("verde")
    case "amarillo":
        print("amarillo")
    case _:
        print("error")

# FUNCIONES -------------------------------------------------------------- def
def sumar (primero, segundo):
    return primero + segundo

resultado = sumar(1,2)
print(resultado)

# BUCLES ------------------------------------------------------------------ for

Animales = ("perro", "gato", "vaca")

for animal in Animales:
    print(animal)

##
# ALGORITMOS BASICOS-------------------------------------------------------------
class Persona:
    #Se usa "__init__" para el metodo constructor de un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola :U me llamo {self.nombre} y tengo {self.edad} años."
    #"self" es el quivalente a this, en C#, y hace referencia al mismo objeto en el interprete

#Lista de Personas
personas = [
    Persona("Juan", 25),
    Persona("Maria", 30),
    Persona("Carlos", 22)
]

#Busqueda Secuencial
def BusquedaSecuencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

#Busqueda de Objetos
def buscar_persona(lista_personas, nombre):
    for persona in lista_personas:
        if persona.nombre == nombre:
            return persona
    return None #"None" es el equivalente a default o Null en C#

# Buscar una persona por su nombre
nombre_buscado = "Maria"
persona_encontrada = buscar_persona(personas, nombre_buscado)

# Mostrar resultados
if persona_encontrada:
    print(persona_encontrada.saludar())
else:
    print(f"No hay coincidencia de la persona con el nombre {nombre_buscado}.")