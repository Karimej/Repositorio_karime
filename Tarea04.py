#Tarea 4
#Resolver los siguientes ejercicios

#Considera las siguientes calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4

#Calcula el promedio de las calificaciones considerando que:
## 1era nota vale 15% del total
## 2da nota vale 35% del total
## 3era nota vale 50% del total

valor1 = 0.15
valor2 = 0.35
valor3 = 0.50

prom_ponderado = (calif_1 * valor1) + (calif_2 * valor2) + (calif_3 * valor3)
promedio1 = prom_ponderado/3
print(promedio1)


#La siguiente matriz debe cumplir que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores
#Crea un código para hacer las correcciones necesarias

matriz = [[1,1,1,3], [2,2,2,7],[3,3,3,9],[4,4,4,13]]

for fila in matriz:
    suma = sum(fila[:3])
    fila[3] = suma

for fila in matriz:
    print(fila)
