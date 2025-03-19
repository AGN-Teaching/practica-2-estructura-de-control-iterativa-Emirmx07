# Función para cifrar un mensaje con el cifrado César
def cifrar(mensaje, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    mensaje_cifrado = ""
    
    posicion = 0  # Para recorrer el mensaje
    tamaño_mensaje = 0  # Contador del tamaño del mensaje

    # Contar cuántos caracteres hay en el mensaje
    while mensaje[tamaño_mensaje:tamaño_mensaje+1] != "":
        tamaño_mensaje = tamaño_mensaje + 1

    while posicion < tamaño_mensaje:
        letra = mensaje[posicion:posicion+1]  # Obtener cada letra
        
        # Buscar en el abecedario
        posicion_letra = 0
        while posicion_letra < 26:  
            if abecedario[posicion_letra:posicion_letra+1] == letra:
                nueva_posicion = posicion_letra + desplazamiento
                
                # Si se pasa del final, regresar al inicio
                if nueva_posicion >= 26:
                    nueva_posicion = nueva_posicion - 26
                
                mensaje_cifrado = mensaje_cifrado + abecedario[nueva_posicion:nueva_posicion+1]
                break  # Dejar de buscar la letra

            posicion_letra = posicion_letra + 1
        else:
            # Si no es una letra, se agrega igual
            mensaje_cifrado = mensaje_cifrado + letra

        posicion = posicion + 1

    return mensaje_cifrado


# Ejemplo de uso
mensaje_original = "hola"
desplazamiento = 3  # Cambia esto para otro cifrado
mensaje_cifrado = cifrar(mensaje_original, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)
