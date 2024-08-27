# Tarea 2
## Instrucciones
# Crear un script donde se imprima un ejemplo de cada método listado

print ("Ejemplo de la función list.append(x)")
mi_lista = ["Comí","una","manzana"]
mi_lista.append("ayer")
print(mi_lista)

print("Ejemplo de la función list.extend(iterable)")
# Creamos una segunda lista para agregarla
segunda_lista = ["y","me","gustó"]

mi_lista.extend(segunda_lista)
print(mi_lista)

print("Ejemplo de una función list.insert(i,x)")
mi_lista.insert (3,"amarilla")
print (mi_lista)

print("Ejemplo de una función list.remove (x)")
mi_lista.remove ("amarilla")
print(mi_lista)

print ("Ejemplo de una función list.pop([i])")
ultimo_elemento = mi_lista.pop()
print ("Elemento eliminado:", ultimo_elemento)
print ("Lista despues de pop:", mi_lista)

print ("Ejemplo de una función list.clear()")
mi_lista.clear()
print ("Lista despues de clear:", mi_lista)

print ("Ejemplo de una función list.index(x[, start[, end]])")
mi_lista = [1, "dos", 3, 4, 5]
print(mi_lista)
indice_dos = mi_lista.index("dos")
indice_dos_desde_1 = mi_lista.index("dos",1)

print("La palabra dos se encuentra en el índice:", indice_dos)

print ("Ejemplo de una función list.count(x)")
# Creamos una nueva lista
lista_numeros = [1, 2, 2, 3, 2, 4, 6]
conteo_2 = lista_numeros.count(2)
print ("El número 2 aparece:",conteo_2, "veces en la lista" )

print ("Ejemplos de una función list.sort(*, key=None, reverse=False)")
lista_numeros.sort()
print("Lista ordenada en orden ascendente:", lista_numeros)
lista_numeros.sort(reverse=True)
print("Lista ordenada en orden descendente", lista_numeros)

print ("Ejemplos de una función list.reverse()")
lista_numeros.reverse()
print("Lista de nuevo en orden ascendente:", lista_numeros)

print("Ejemplos de una función list.copy()")
lista_numeros2 = lista_numeros.copy()
print("Lista copiada:", lista_numeros2)









