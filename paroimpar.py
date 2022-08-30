
# ENUNCIADO DEL PROYECTO: Par o impar
# Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000.
# Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.
#     Ejemplo:
#     Mensaje que se muestra: ¿En qué número estás pensando?
#     Entrada: 25
#     Salida: ¡Es un número impar! ¿Puedes añadir otro?
 

def test(num):
    if num > 1000:
        print('Por favor inserte un número del 1 al 1000')
    elif num < 0:
        print('Por favor inserte un número del 1 al 1000')
    else: 
        if num % 2 == 0:
            print(' El número es par')
        else:
            print(' El número es impar')
        return
    return 


#Ejecución de la función
def run():
    num = int(input('Inserte un número del 1 al 1000: '))
    test(num)
    return    

if __name__ == '__main__':
    run()