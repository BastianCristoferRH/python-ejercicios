# Slicing en Python

## Qué es Slicing?

El slicing es una forma de extraer partes de una cadena, lista o tupla usando índices.

Sintaxis: [inicio:fin:paso]

---

## Un solo : (inicio:fin)

Extrae desde inicio hasta fin-1 (fin NO se incluye)

Ejemplo:
texto = "Python"
texto[1:4]      # "yth"  (índices 1, 2, 3)
texto[:3]       # "Pyt"  (desde el inicio hasta índice 2)
texto[3:]       # "hon"  (desde índice 3 hasta el final)

---

## Índices Negativos

Los índices negativos cuentan desde el final:

texto = "Python"
texto[-1]       # "n"    (último carácter)
texto[-3:]      # "hon"  (últimos 3 caracteres)
texto[:-1]      # "Pytho" (todo excepto el último)

---

## Doble :: (inicio:fin:paso)

El paso controla cada cuántos elementos tomar:

texto = "Python"

# Paso positivo (hacia adelante)
texto[::2]      # "Pto"   (cada 2 caracteres)
texto[1::2]     # "yhn"   (desde índice 1, cada 2)

# Paso negativo (invierte)
texto[::-1]     # "nohtyP" (INVIERTE la cadena)

---

## Tabla Rápida

| Código | Resultado | Qué hace |
|--------|-----------|----------|
| [2] | 1 carácter | Obtiene índice 2 |
| [1:4] | 3 caracteres | Del índice 1 al 3 |
| [:3] | Primeros 3 | Desde inicio hasta 2 |
| [3:] | Últimos 3 | Desde 3 hasta el final |
| [-2:] | Últimos 2 | Del penúltimo al final |
| [::2] | Salto de 2 | Cada 2 caracteres |
| [::-1] | INVERTIDO | Voltea toda la cadena |

---

## Reglas Importantes

1. El fin NUNCA se incluye en el resultado
2. Los índices negativos cuentan desde el final
3. Si omites valores, Python asume inicio/fin automáticos
4. Paso negativo invierte la dirección

---

## Ejemplo Práctico

palabra = "Hola"

# Invertir una palabra
palabra[::-1]           # "aloH"

# Tomar cada 2 letras
palabra[::2]            # "Hl"

# Excluir primero y último
palabra[1:-1]           # "ol"

---

## Casos de Uso Comunes

# Primeros 3 elementos
lista = [1, 2, 3, 4, 5]
lista[:3]               # [1, 2, 3]

# Últimos 2 elementos
lista[-2:]              # [4, 5]

# Elementos intermedios
lista[1:4]              # [2, 3, 4]

# Invertir lista
lista[::-1]             # [5, 4, 3, 2, 1]

# Cada 2 elementos
lista[::2]              # [1, 3, 5]
