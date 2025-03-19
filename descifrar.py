# descifrar.py - Descifra un mensaje usando el cifrado César

def descifrar(mensaje, k):
    resultado = ""  
    indice = 0  

    # Recorrer el mensaje a un lado mientras
    while mensaje[indice:]:  
        letra = mensaje[indice]

        # Verificar si la letra es mayúscula
        if 'A' <= letra <= 'Z':
            nueva_letra = chr(((ord(letra) - ord('A') - k) % 26) + ord('A'))
        # Verificar si la letra es minúscula
        elif 'a' <= letra <= 'z':
            nueva_letra = chr(((ord(letra) - ord('a') - k) % 26) + ord('a'))
        else:
            nueva_letra = letra  # No se cifra

        resultado = resultado + nueva_letra
        indice = indice + 1  # Avanzamos al siguiente carácter
    
    return resultado

# Programa principal para descifrar
mensaje_cifrado = input("Ingresa el mensaje cifrado: ")
k = int(input("Ingresa el número de desplazamiento usado en el cifrado: "))

mensaje_descifrado = descifrar(mensaje_cifrado, k)
print("Mensaje descifrado:", mensaje_descifrado)

