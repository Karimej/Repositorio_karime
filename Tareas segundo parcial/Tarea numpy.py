from typing import Any

import numpy as np
from fontTools.cffLib import encodeNumber
from numpy import ndarray, dtype, signedinteger

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
print("Ejercicio 1")
freq = np.random.randint(1,8, size=4)
print(freq)

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
print("Ejercicio 2")
amplitud = np.random.uniform (3,6, size=4)
print(amplitud)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]
print("Ejercicio 3")
t = np.arange(0,1,1/2000)
print(t)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Hint: recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t) donde A es la amplitud y B es la
# frecuencia. Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
amplitud = [2, 1, 1.5, 4]
frecuencia = [1, 2, 5, 3]

plt.figure(figsize=(10, 8))

for i in range(4):
    ondas = amplitud[i] * np.sin(frecuencia[i] * t)
    plt.plot(t, ondas, label=f"Amplitud: {amplitud[i]}, Frecuencia: {frecuencia[i]} Hz")

plt.title("Ondas")
plt.xlabel("tiempo")
plt.ylabel("amplitud")
plt.legend()

plt.grid(True)
plt.show()

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales
# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
#X = np.fft.fft(x)

x = sum(ondas)
plt.plot(t, x, label="Suma de ondas")
plt.title("Suma de 4 Ondas Sinusoidales")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

print(x[:10])

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
print("Ejercicio 6")
frequence = np.arange(0,1999)
print(frequence)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
print("Ejercicio 7")
x = np.array([x])
x_abs = np.abs(x)
print(x_abs)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
print("Ejercicio 8")
ind_max = np.argsort(x)[-4:]
val_max = x[ind_max]
print("4 elementos máximos:",val_max)
print("Índices de elementos:", ind_max)
