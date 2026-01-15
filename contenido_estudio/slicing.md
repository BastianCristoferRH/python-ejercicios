#  Slicing en Python

## ¿Qué es Slicing?

El slicing es una forma de extraer partes de una cadena, lista o tupla usando índices.

**Sintaxis:** [inicio:fin:paso]

---

##  Un solo : (inicio:fin)

Extrae desde inicio hasta in-1

\\\python
texto = "Python"
texto[1:4]      # "yth"  (índices 1, 2, 3)
texto[:3]       # "Pyt"  (desde el inicio hasta índice 2)
texto[3:]       # "hon"  (desde índice 3 hasta el final)
\\\

---

##  Índices Negativos

Los índices negativos cuentan desde el final:

\\\python
texto = "Python"
texto[-1]       # "n"    (último carácter)
texto[-3:]      # "hon"  (últimos 3 caracteres)
texto[:-1]      # "Pytho" (todo excepto el último)
\\\

---

##  Doble :: (inicio:fin:paso)

El paso controla cada cuántos elementos tomar:

\\\python
texto = "Python"

# Paso positivo (hacia adelante)
texto[::2]      # "Pto"   (cada 2 caracteres)
texto[1::2]     # "yhn"   (desde índice 1, cada 2)

# Paso negativo (invierte)
texto[::-1]     # "nohtyP" (INVIERTE la cadena)
\\\

---

##  Tabla Rápida

| Código | Resultado | Qué hace |
|--------|-----------|----------|
| \[2]\ | 1 carácter | Obtiene índice 2 |
| \[1:4]\ | 3 caracteres | Del índice 1 al 3 |
| \[:3]\ | Primeros 3 | Desde inicio hasta 2 |
| \[3:]\ | Últimos 3 | Desde 3 hasta el final |
| \[-2:]\ | Últimos 2 | Del penúltimo al final |
| \[::2]\ | Salto de 2 | Cada 2 caracteres |
| \[::-1]\ | INVERTIDO | Voltea toda la cadena |

---

##  Reglas Importantes

 El **fin NUNCA se incluye** en el resultado  
 Los índices **negativos** cuentan desde el final  
 Si omites valores, Python asume inicio/fin automáticos  
 **Paso negativo** invierte la dirección

---

##  Ejemplo Práctico

\\\python
palabra = "Hola"

# Invertir una palabra
palabra[::-1]           # "aloH"

# Tomar cada 2 letras
palabra[::2]            # "Hl"

# Excluir primero y último
palabra[1:-1]           # "ol"
\\\

