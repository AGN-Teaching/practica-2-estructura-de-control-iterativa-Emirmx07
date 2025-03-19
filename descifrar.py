# Función para descifrar un mensaje cifrado con el cifrado César
def descifrar(mensaje, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    mensaje_descifrado = ""
    
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
                nueva_posicion = posicion_letra - desplazamiento
                
                # Si se pasa del inicio, regresar al final
                if nueva_posicion < 0:
                    nueva_posicion = nueva_posicion + 26
                
                mensaje_descifrado = mensaje_descifrado + abecedario[nueva_posicion:nueva_posicion+1]
                break  # Dejar de buscar la letra

            posicion_letra = posicion_letra + 1
        else:
            # Si no es una letra, se agrega igual
            mensaje_descifrado = mensaje_descifrado + letra

        posicion = posicion + 1

    return mensaje_descifrado


# Ejemplo de uso
mensaje_cifrado = "krod"
desplazamiento = 3  # Debe ser el mismo que se usó para cifrar
mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado
