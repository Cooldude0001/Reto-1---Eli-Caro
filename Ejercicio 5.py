# Ejercicio 5
def same_caracters (String_lista): 
    """Esta función evalúa qué elementos de la lista contienen los mismos caracteres --> anagramas."""
    
    # Filtro para tipos de datos no válidos
    for cada_elemento in String_lista:
        if cada_elemento.isdigit ():
            print ("La lista contiene tipos de datos no validos")
            return None
    
    # Lista para almacenar los anagramas encontrados
    Final_list = []

    # Comparación de anagramas
    for repeticion in range (len (String_lista)): # Recorre la lista
        for elemento_comparable in range (repeticion + 1, len (String_lista)): # Recorre el indice consecutivo del ciclo anterior
            
            # Ordenar los caracteres de ambas palabras para compararlos
                # Como tienen los mismos caracteres entonces cuando se organicen alfabeticamente, estos seran iguales y se añadiran a "Final_list"
            if sorted (String_lista [repeticion]) == sorted (String_lista [elemento_comparable]):
                Final_list.append ([String_lista [repeticion], String_lista [elemento_comparable]]) 
    
    # Resultados de la comparación
        # Si la lista no esta vacia, se imprimen los anagramas encontrados y retorna "Final_list"
    if len (Final_list) != 0:
        print("Anagramas encontrados en la lista proporcionada:", Final_list)
        return Final_list
    else:
        print("No se encontraron anagramas en la lista que proporciono")
        return None

# Ejemplo de uso
lista = ["rosa", "roma", "mora", "amor", "sora", "pepe", "perro", "manzana"]
same_caracters (lista)