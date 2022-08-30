# ENUNCIADO: Contador de palabras
# Preguntamos al usuario en que está pensando. 
# Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.
# Ejemplo:
# Pregunta: ¿En qué estás pensando?
# Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
# Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!
# Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas frases, y contamos cuántas palabras tiene y lo imprimimos.

def cont_palabras(frase):
    div = frase.split()
    print ('Me dijiste tu pensamiento en tan solo '+ str(len(div)) + ' palabras.')


def run():
    frase = input('¿En qué estás pensando? : ')
    cont_palabras(frase)

if __name__ == '__main__':
    run()