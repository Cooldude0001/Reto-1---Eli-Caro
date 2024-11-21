# Ejercicio palindromo
def palindromeVerifier (palabra = None):
    """Esta función verifica que la palabra proporcionada sea un palindromo,
    retornando 'True' en el caso de que la palabra sea uno y 'False' en caso negativo."""

    # En caso de que el usuario no ingrese un argumento valido
    if palabra == None:
        print ("Debe ingresar un argumento a la función")
        return None

    # Verificación del tipo de dato que proporciono el usuario
    if palabra.isdigit ():
        print ("Debe ingresar palabras")
        return None
    
    # Minusculización de la palabra que ingreso el usuario
    palabra = palabra.lower ()

    # Revertir la palabra original para ver si es un palindromo
    Supuesto_palindromo = ""
    indice = -1
    
    for i in palabra: # El ciclo itera por cada letra que tenga la palabra 
        constructor = (palabra [indice]) # Toma la última letra de la palabra
        indice -= 1

        Supuesto_palindromo = Supuesto_palindromo + constructor
    
    # Verificacion de la similitud entre el supuesto palindromo y al palabra proporcionada
        # Caso en el que la palabra no sea un palindromo
    if Supuesto_palindromo != palabra:
        print ("La palabra que ingreso no es un palíndromo")
        return False 

        # Caso en el que la palabra no sea un palindromo
    if Supuesto_palindromo == palabra:
        print ("La palabra que ingreso es un palíndromo")
        return True

# Ejemplo de uso
palindromeVerifier ("Hannah")
palindromeVerifier ("Carlos")