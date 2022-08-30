# ENUNCIADO: ¿CÚAL ES MI ACRÓNIMO?
# Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y con ello como resultado obtendremos el acrónimo. Por ejemplo:
# Entrada -> As Soon As Possible. Salida -> ASAP.
# Entrada -> World Health Organization. Salida -> WHO.
# Entrada -> Absent Without Leave. Salida -> AWOL.

#Utilizamos estas librerías para intentar voltear el output del código
import pandas as pd
import numpy as np

def acro(palabra):
    desag = palabra.split() # Dividimos palabra y la convertimos en lista para trabajarla.
    n = len(desag)
    for i in range (0,n):
        list = desag[i]
        y = [list[0].capitalize()]
        t = np.transpose(y)
        print(np.transpose(t))
   
        


def run():
    palabra = input('Ingrese la palabra: ')  
    acro(palabra)
    

if __name__=='__main__':
    run()