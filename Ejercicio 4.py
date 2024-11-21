# recibir una lista de numeros enteros y retornar la mayor suma entre dos elementos consecutivos
def Consecutive_sum (lista):
    """Esta función realiza una suma con los elementos consecutivos y devuelve la que sea mayor."""
    # Revisión de que todos los elementos sean números enteros
    for cada_elemento in lista:
        if type (cada_elemento) == int:
            continue
        else:
            print ("La lista que ingreso contiene elementos no válidos (no númericos)")
            return None      
    
    # Suma de elementos consecutivos
    sumas = [] # Lista que lmacena las sumas parciales
    indice = 1 # Indice del elemento consecutivo

        # Realización de las sumas
    for numero in lista:    
        # Para evitar una excepción del tipo indexerror
        if indice == len (lista):
            break

        Suma_parcial = numero + lista [indice]

        sumas.append (Suma_parcial)
        indice += 1
    
    # Organización de los elementos de la lista "sumas"
    sumas.sort ()
    print (f"La mayor suma de elementos consecutivos es: {sumas [-1]}")
    return (sumas [-1])

# Ejemplo de uso
Lista = [1,2,6,7,5,3,4,8,1,3,5]
Consecutive_sum (Lista)