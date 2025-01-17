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
        
# FUNCIONES --------------------------------------------------------------
def sumar (primero, segundo):
    return primero + segundo

resultado = sumar(1,2)
print(resultado)

# BUCLES ------------------------------------------------------------------

Animales = ("perro", "gato", "vaca")

for animal in Animales:
    print(animal)

##
# ALGORITMOS BASICOS-------------------------------------------------------------
