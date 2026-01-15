#Invertir una cadena
#ejemplo de cadena: "Hola" a "aloH"

palabra  = "ricardo"

def invertir_palabra(palabra):
    palabra_invertida = ""
    for letter in palabra:
        palabra_invertida = letter + palabra_invertida
    return palabra_invertida

def invertir_palabra_recursivo(palabra):
    if len(palabra) == 0:
        return palabra
    else:
        aux = palabra[-1] + invertir_palabra_recursivo(palabra[:-1])
        return aux        
    
print(invertir_palabra(palabra))
print(invertir_palabra_recursivo(palabra))
print(palabra[::-1]) 



