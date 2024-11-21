# Logica de resolución de ejercicios
Este readme contiene los procesos para dar solución a cada ejercicio del reto uno:


Ejercicio 1: Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Realizar este ejercicio fue relativamente sencillo, la función recibe 2 argumentos númericos de tipo int llamados numero_1, numero_2 y uno de tipo str referente al signo de la operación que se quiere realizar, luego los argumentos pasan por 2 filtros, el primero manejado por un if que evalúa que numero_1 y numero_2 solo sean de tipo int y un ciclo for que evalua que el signo que se proprciono corresponda a alguna de las operaciones básicas, si en ambos casos no se cumplen estas condiciones se notifica al usuario y retorna None, en caso de que lo anterior no se cumpla los argumentos pasan a una variable llamada Operacion, que luego se utiliza para definir la varible Resultado_op, que utiiza la función eval para determinar el resultado de la operación, una vez hecha esta se muestra al usuario y se devuelve.

Ejercicio 2: Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
Para realizar este ejercicio, primero defini que el valor predeterminado de la variable palabra 

Ejercicio 3: Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Ejercicio 4: Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Ejercicio 5: Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
