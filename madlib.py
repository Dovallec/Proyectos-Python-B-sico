# ENUNCIADO DEL PROYECTO: JUEGO DEL MAD LIB
# Pedimos al usuario que introduzca varias entradas con varias preguntas.
# Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o incluso una acción. 
# Una vez que se obtiene la entrada, se puede reorganizar para construir su propia historia.

#soy un (sustantivo) me caracterizo por (adjetivo)  tengo (numero) dias que estoy en la carcel por cometer un (verbo)  en (ciudad)    

def run():
    sustantivo = input('Dime un sustantivo: ')
    adjetivo = input('Dime un adjetivo: ')
    numero = input('Dime un numero: ')
    verbo = input('Dime un verbo: ')
    ciudad = input('Dime una ciudad: ')
    print ('Soy un '+ sustantivo +' , me caracterizo por '+ adjetivo +  ' llevo ' + numero + ' meses en la carcel por ' + verbo +  ' en ' + ciudad + '.' )

if __name__ == '__main__':
    run()
