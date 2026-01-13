#Caular el factorial de forma iterativa y recursiva

def factorial(n):
    aux = 1
    while n > 1:
        aux*= n
        n -=  1
    return aux
    

def factorial_recursivo(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursivo(n-1)

#imprimir factorial 
print(factorial(5)) 
#imprimir factorial recursivo 
print(factorial_recursivo(5))