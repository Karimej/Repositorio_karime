#Tarea 3
#Crear un ejemplo con cada método de diccionario

#Función pop
#Elimina el elemento con la clave especificada
print("Ejemplo de una función pop()")
basura = {
    "verde": "orgánica",
    "gris": "inorgánica",
    "azul": "papel"
}
basura_eliminada = basura.pop("azul")
print(basura)
print(basura_eliminada)

#Función get
#Devuelve el valor de la clave especificada
print("Ejemplo de una función get()")
basura2 = basura.get("gris")
print(basura2)

#Función copy
#Devuelve una copia del diccionario
print("Ejemplo de una función copy()")
basuracopia=basura.copy()
print(basuracopia)

#Función keys
#Devuelve una lista que contiene las claves del diccionario
print("Ejemplo de una función keys()")
basurakeys = basura.keys()
print(basurakeys)

#Función items
#Devuelve una lista que contiene una tupla para cada par de valores clave
print("Ejemplo de una función items()")
basurai = basura.items()
print(basurai)

#Función clear
#Eliminar todos los elementos del diccionario
print("Ejemplo de una función clear()")
basura.clear()
print(basura)

#Función fromkeys
#Devuelve un diccionario con las claves y el valor especificados
print("Ejemplo de una función fromkeys()")
nueva_clave = ["ana", "alisson", "anette"]
nuevo_dic = dict.fromkeys(nueva_clave,2)
print(nuevo_dic)

#Función popitem
#Elimina el último par clave-valor insertado
print("Ejemplo de una función popitem()")
par = nuevo_dic.popitem()
print("Valor eliminado:", par)
print("Diccionario actualizado:", nuevo_dic)

#Función setdefault
#Devuelve el valor de la clave especificada
print("Ejemplo de una función setdefault()")
edades = {"Ana":20, "Alisson":26, "Anette":17}
edad_anette = edades.setdefault("Anette")
print("Edad de Anette:", edad_anette)

#Función update
#Actualiza el diccionario con los pares clave-valor especificados
print("Ejemplo de una función update()")
edades.update ({"Alan": 22})
print(edades)

#Función values
#Devuelve una lista de todos los valores en el diccionario
print("Ejemplo de una función values()")
valores = edades.values()
print(edades)