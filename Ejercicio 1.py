# Funcion operaciones básicas
def b_operations (numero_1, numero_2, operacion):
    """Funcion que realiza operaciones aritméticas entre dos números enteros y un signo
    proporcionados por el usuario siguiendo la siguiente estructura: Entrada: (1, 2, "+")
    Salida: 3."""
    
    # Verificaciones de tipos de datos
        # Verificación de que los argumentos "números" sean enteros
    if type (numero_1) != int or type (numero_2) != int:
        print ("No ha ingresado números enteros a la función")
        return None
    else:
        numero_1 = str (numero_1) ; numero_2 = str (numero_2)

        #  Validación del signo proporcionado
    Signos_validos = ["+", "-", "*", "/"]
    
    if operacion not in Signos_validos:
        print ("No se puede realizar una operación válida con el signo que proporciono")
        return None

    # Operaciones y entrega de resultados
    Operacion = numero_1 + operacion + numero_2
    Resultado_op = eval (Operacion)
    
    print (f"El resultado de {numero_1}{operacion}{numero_2} es {Resultado_op}")
    return Resultado_op

# Ejemplo de uso
b_operations (9, 5, "*")