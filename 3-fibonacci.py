
def fibonacci(n):
    valores=[]
    a,b = 0,1
    for i in range(n):
     aux = a
     a=b
     b=aux + b
     valores.append(aux)
    return valores


def fibonacci_recursivo(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        aux = fibonacci_recursivo(n - 1)
        aux.append(aux[-1] + aux[-2])
        return aux  

print(fibonacci(7))
print(fibonacci_recursivo(7))
