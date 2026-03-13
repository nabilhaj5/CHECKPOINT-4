# Ejercicio 1: Crea lista, tupla, float, int, decimal, dict
lista_colores = ["blanco","rojo","amarillo"]
tupla_colores=("uno","dos","tres")
flotante= 5.3
entero=10
decimal=3.14
diccionario={"nombre":"nabil"}
# Ejercicio 2: Redondea arriba
import math
print(math.ceil(flotante))
# Ejercicio 3: Raíz cuadrada
print(math.sqrt(flotante))
# Ejercicio 4: Primer elemento dict
print(next(iter(diccionario)))
#Ejercicio 5: Segundo de tupla  
segundo_elemento=tupla_colores[1]
print(segundo_elemento)  # "dos"
# Ejercicio 6: Append final lista
print(lista_colores[:1])
lista_colores.append("castaño")
print(lista_colores)
# Ej7: Reemplaza primero
lista_colores[0]="verde"
print(lista_colores)
# Ej8: Sort alfabético
lista_colores.sort()
print(lista_colores)
# Ej9: Reasigna tupla
tupla_colores+=("cuatro",)
print(tupla_colores)
suma=2*(5+1)+5-5**2
print(suma)