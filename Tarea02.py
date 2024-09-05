# Tarea 2
# Determinar si la función range cumple con las siguientes características

#Establecemos un rango
rango = range(6)

# Mutabilidad
try:
    rango[0]=5
except TypeError:
    print("Range es inmutable")
else:
    print("Range es mutable")

# Range es INMUTABLE

# Suma
rango2 = range(1,7)
sumaesperada = 21
suma = sum(rango2)

if suma == sumaesperada:
    print("Suma cumple con valor esperado")
else:
    print("Suma no cumple con valor esperado")

# Producto por un entero
rango3=range(1,12)
n=2
# Verificar que todos los elementos son multiplos de n
multiplos= all(x%n == 0 for x in rango3)
print("múltiplos de n",multiplos)

# Slicing
rango4 = range(2,21)
subrango = rango[4:17]

if subrango == rango[4:17]:
    print("Range cumple slicing")
    print(list(subrango))
else:
    print("Range no cumple slicing")

# Convertir a lista o tupla
rango5 = range(1,19)
print(rango5)

if isinstance(rango5,range):
    lista=list(rango5)
    print("Lista",lista)
    tupla=tuple(rango5)
    print("Tupla",tupla)
else:
    print("Dato no es de tipo rage")

# Función len
rango6=range(9)
print("Rango:",list(rango6))

longitud = len(rango6)
print("Longitud:",longitud)









