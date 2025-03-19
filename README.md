# Práctica 2. Estructura de control iterativa

## Presentación del Problema

En esta práctica, se nos pide  que diseñemos un programa en Python para cifrar y descifrar mensajes utilizando un método de sustitución basado en desplazamiento de caracteres. El objetivo principal es transformar un mensaje original en una versión cifrada que solo pueda ser recuperada mediante un proceso inverso.

El problema que se nos plantea en la practica consiste en implementar un algoritmo que permita aplicar un desplazamiento "k" a cada carácter del mensaje, para asegurar que pueda ser descifrado correctamente cuando se conozca la letra  k.

## Diseño del Algoritmo

Para resolver este problema, se utilizaron los siguientes conceptos:

### Incorporación de "k" en el mensaje

El valor de k representa el desplazamiento de los caracteres en el alfabeto. Se incluye como un parámetro ingresado por el usuario y se aplica a cada letra del mensaje para transformarlo. En el cifrado, k se suma al valor del carácter para obtener su equivalente cifrado. En el descifrado, k se resta para recuperar el mensaje original.

### 1. **Listas**
Se usaron listas para almacenar el mensaje convertido en una secuencia de caracteres, facilitando su manipulación en el proceso de cifrado y descifrado.

### 2. **Strings**

Se emplearon cadenas de texto para manejar la entrada del usuario y el almacenamiento del mensaje antes y después del cifrado.

### 3. **Estructura de Control Secuencial**

Se aplicó una secuencia de instrucciones que permiten capturar el mensaje, realizar el cifrado o descifrado y mostrar los resultados al usuario.

### 4. **Estructura de Control Selectiva Simple**

Se usó para validar si el usuario desea cifrar o descifrar el mensaje, ejecutando la acción correspondiente.

### 5. **Estructura de Control Selectiva Anidada**

Se implementó para verificar si un carácter pertenece al alfabeto y aplicar el desplazamiento k solo a los caracteres alfabéticos, dejando intactos otros símbolos o espacios.

### 6. **Estructura de Control Selectiva Múltiple**

Se utilizó if-elif-else para manejar diferentes casos de entrada, asegurando que solo se procesen caracteres válidos y permitiendo al usuario elegir entre cifrar o descifrar.

### 7. **Estructura de Control Iterativa con Control Previo**

Se utilizó una estructura iterativa con control previo para recorrer cada carácter del mensaje y aplicar la transformación correspondiente. La condición se evalúa antes de ejecutar el bloque de instrucciones, asegurando que el proceso se realice de manera controlada.
### 8. **Estructura de Control Iterativa con un Número Determinado de Iteraciones**

Se implementó una estructura iterativa con un número definido de repeticiones para recorrer la lista de caracteres del mensaje. Esta iteración se ejecuta tantas veces como caracteres tenga el mensaje, asegurando que cada uno sea procesado correctamente.

## Implementación en Python

El programa solicita al usuario los siguientes datos de entrada:

Mensaje a cifrar o descifrar.

Valor de desplazamiento k.

Opción de cifrado o descifrado.

Para terminar lo que hace el programa, aplica el desplazamiento adecuado a cada carácter del mensaje, transformándolo en su versión cifrada o descifrada. Finalmente, se imprime el mensaje resultante.

## Comentarios 
Que  hayamos aprendido el uso de listas facilitó el poder manejar los caracteres en el proceso que hacia el codigo del cifrado y descifrado. Aparte que, las estructuras de control selectivas permitieron validar correctamente las entradas del usuario y aplicar las transformaciones necesarias en cada caso.

En conclusión, la práctica ayudo a reforzar el uso de estructuras selectivas en Python y su aplicación en un problema de seguridad de información como el cifrado de mensajes, ademas que aplicamos nuevos temas como "Estructura de control iterativa con control previo" y "Estructura de control iterativa con un número determinado de iteraciones" estos temas ayudan a mejorar en las practicas futuras y en esta ya que entre mas temas aprendamos mejor sera nuestra compresion hacia problemas o practicas nuevas.
