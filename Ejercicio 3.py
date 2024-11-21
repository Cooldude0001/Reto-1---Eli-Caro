# Ejercicio números primos en una lista
def prime_finder (lista):
    """Esta función encuentra y devuelve los números primos que se encuentren dentro
    de la lista de números enteros proporcionada."""

    # Revisión de que todos los elementos sean números enteros
    for cada_elemento in lista:
        if type (cada_elemento) == int:
            continue
        else:
            print ("La lista que ingreso contiene elementos no válidos (no númericos)")
            return None
                   
    # Obtencion de numneros primos de la lista
        # Obtención de los divisores de cada número
     
    Numeros_primos = [] # Lista en el que se almacenan los números primos encontrados
        
        # En este caso se supone que todos los elementos de la lista son primos hasta
        # demostrar lo contrario, representado en la variable Validez

    for numero in lista:
            
        Validez = True

        # Aqui se generan los divisores del numero
        for Divisores in range (2, int (numero**0.5) + 1):
            if numero % Divisores == 0:
                Validez = False
                break
        
        # 1 no se considera un numero primo  
        if numero < 2:
            Validez = False

        if Validez == True:
            Numeros_primos.append (numero)

        Validez = True # Reinicio de la variable Validez para seguir agregando elementos 
                       # a la lista Numeros_primos 

    if len (Numeros_primos) == 0:
            print ("Dentro del rango que ingreso no existen numeros primos")
            return None
    else:
        print (f"Los numeros primos encontrados son: {Numeros_primos}")
        return Numeros_primos       

# Ejemplo de uso
Lista = [1, 3, 4, 56, 97, 1542, 163,33, 47]
prime_finder (Lista)