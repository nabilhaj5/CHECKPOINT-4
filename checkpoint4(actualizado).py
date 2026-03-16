# Ejercicio 1: Crea lista, tupla, float, int, decimal, dict
from decimal import Decimal  
lista_colores = ["blanco", "rojo", "amarillo"]
tupla_colores = ("uno", "dos", "tres")
flotante = 5.3           # float
entero = 10              # int
decimal_num = Decimal("3.14")  # decimal con módulo Decimal
diccionario = {
    "nombre": "Nabil",
    "edad": 30,
    "curso": "Python",
    "ciudad": "Vitoria"}
print(lista_colores)
print(tupla_colores)
print(flotante)
print(entero)
print(decimal_num)
print(diccionario)


# Ejercicio 2: # Ejercicio 2: para Redondear punto flotante hacia arriba
import math
print(math.ceil(flotante))

# Ejercicio 3: Raíz cuadrada
print(math.sqrt(flotante))

# Ejercicio 4:  para Seleccionar el primer elemento del diccionario
print(next(iter(diccionario)))    # primera clave

#Ejercicio 5: para seleccionr el Segundo de la tupla  
segundo_elemento=tupla_colores[1]
print(segundo_elemento)  # "dos"

# Ejercicio 6: para agregar un elemento al  final de la lista
print(lista_colores[:1])
lista_colores.append("castaño")
print(lista_colores)

# Ejercicio 7:  para Reemplaza el primer elemento de mi lista
lista_colores[0]="verde"
print(lista_colores)

# Ejercicio 8: para Ordenar mi lista alfabéticamente
lista_colores.sort()
print(lista_colores)

# Ejercicio 9: Uso la reasignación para agregar un elemento a tu tupla
tupla_colores+=("cuatro",)
print(tupla_colores)
suma=2*(5+1)+5-5**2
print(suma)