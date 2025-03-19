def cifrar(mensaje, k):
    resultado = ""  
    indice = 0  

    # Recorrer el mensaje con a un lado mientras
    while mensaje[indice:]:  
        letra = mensaje[indice]

        # Verificar si la letra es mayúscula
        if 'A' <= letra <= 'Z':
            nueva_letra = chr(((ord(letra) - ord('A') + k) % 26) + ord('A'))
        # Verificar si la letra es minúscula
        elif 'a' <= letra <= 'z':
            nueva_letra = chr(((ord(letra) - ord('a') + k) % 26) + ord('a'))
        else:
            nueva_letra = letra  # No se cifra

        resultado = resultado + nueva_letra
        indice = indice + 1  # Avanzamos al siguiente carácter
    
    return resultado

# Programa principal para cifrar
mensaje = input("Ingresa un mensaje a cifrar: ")
k = int(input("Ingresa el número de desplazamiento (3 a 15): "))

mensaje_cifrado = cifrar(mensaje, k)
print("Mensaje cifrado:", mensaje_cifrado)
