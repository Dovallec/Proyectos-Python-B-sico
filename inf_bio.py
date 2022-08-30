# ENUNCIADO: Información de la biografía
# Pregunte a un usuario su información personal en una sola ronda de preguntas. 
# Luego hay que verificar que la información que se ha ingresado sea válida. 
# Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

# Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, hay que indicar que la entrada es incorrecta y se pide que se ingrese correctamente un nombre válido.

# Cuando se introduce todo correctamente, se muestra un resumen como el que aparece a continuación:

# - Nombre: John Doe
# - Fecha de nacimiento: Jan 1, 1954
# - Dirección: 24 fifth Ave, NY
# - Metas personales: To be the best programmer there ever was.

 #Datos alfanuméricos
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']


def comp_nombre(nombre):
    conj = mayusculas + minusculas
    nombre = nombre.strip().replace(' ','')
    #Revisión de caracteres
    for letra in nombre:
        if letra in conj:
            continue
        else:
            print('El nombre insertado es inválido, tenga en cuenta que el nombre solo debe tener letras. ')
            break
    print('Nombre: ' + nombre)
    return         






def run():
    nombre = input('Ingrese su nombre: ')
    comp_nombre(nombre)
 
    # fecha = input('Ingresa tu fecha de nacimiento DD-MM-AA: ')
    # direccion = input('Ingresa tu dirección: ')
    # metas = input('¿Cuál es tu meta principal?: ')


if __name__=='__main__':
    run()
