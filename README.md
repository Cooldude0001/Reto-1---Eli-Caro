# Orden lógico de resolución de ejercicios
Este readme contiene los procesos para dar solución a cada ejercicio del reto uno:

Se recomienda ver esto cuando no se entienda que hice dentro del código.


# Ejercicio 1
Objetivo: Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Realizar este ejercicio fue relativamente sencillo, la función recibe 2 argumentos númericos de tipo int llamados numero_1, numero_2 y uno de tipo str referente al signo de la operación que se quiere realizar, luego los argumentos pasan por 2 filtros, el primero manejado por un if que evalúa que numero_1 y numero_2 solo sean de tipo int y un ciclo for que evalua que el signo que se proporciono corresponda a alguna de las operaciones básicas, si en ambos casos no se cumplen estas condiciones se notifica al usuario y retorna "_None_".

En caso de que lo anterior no se cumpla los argumentos pasan a una variable llamada Operacion, que después se utiliza para definir la varible Resultado_op, que utiiza la función eval para determinar el resultado de la operación, una vez hecha esta se muestra al usuario y se le devuelve Resultado_Op.

# Ejercicio 2
Objetivo: Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

Para realizar este ejercicio, primero definí dos filtros en donde utilizando el valor predeterminado del argumento palabra sea "_None_", el primer caso en donde el usuario no ingresó ningún argumento y el segundo en donde el argumento no sea una palabra, si esto llega a pasar se le notifica al usuario y la función retorna "_None_".

Una vez realizado, para realizar comparaciones, toda la palabra se pasa minúsculas, se utilizo una variable llamada indice para no recurrir al _slicing_ en donde un ciclo itera para revertir la palabra original, una vez terminado la palabra revertida se guarda en la variable Supuesto_palindromo que se compara con palabra, dependiendo el resultado de la comparación se informa al usuario si lapalabra que proporciono es un palindromo o no, en caso de que lo sea la función devuelve True y si no sea devuelve false.


# Ejercicio 3
Objetivo: Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

_Para este ejercicio se obvio que el usuario va a ingresar una lista con elementos_.

Primero realice un filtro en donde solo se pueda continuar si todos los elementos que contiene la lista proporcionada sean del tipo int, si esto no ocurre se le notificará al usuario.
Para resolver este ejercicio partí del hecho de que un número primo solo tiene dos divisores el mismo y uno, por lo que considere que todos los elementos de la lista son números primos hasta que se demuestre que tiene más divisores, esto se hace utilizado la variable Validez que se tiene un valor booleano True, el ciclo ítera para encontrar los divisores delnúmero proporcionado desde 2 hasta la raíz cuadrada de ese número más uno, esto ya que la función range aproxima hacia abajo y porque los divisores que se encuentren aparecerán antes de la raíz cuadrada de ese número, si el modulo del numero entre su divisor es cero la variable Validez de establecera en Falso, si el numero llega a ser un número primo se añade a la lista Numeros_primos y se devuelve al usuario, si dentro de la lista proporcionada por el usuario no hay números primos se le infomará y se retornara "_None_".

# Ejercicio 4
Objetivo: Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

_Para este ejercicio se obvio que el usuario va a ingresar una lista con elementos_.

Primero realice un filtro en donde solo se pueda continuar si todos los elementos que contiene la lista proporcionada sean del tipo int, si esto no ocurre se le notificará al usuario.
En caso de que la lista pase sin errores el filtro ingresará a un filtro que recorrerá la totalidad de sus elementos y realizará las sumas del elemento de la lista sobre el que está iterando sobre su consecutivo, los resultados de estas sumas se guardan en la variable Suma_parcial, cuyo valor ingresa a la lista sumas, cuando el ciclo termina se utiliza el método sort en la lista sumas, se selecciona su último elemento a través de indexación como la mayor suma entre dos elementos consecutivos, se informa al usuario que cual es el valor de dicha suma y se le entrega dicho valor.

# Ejercicio 5
Objetivo: Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"].

_Para este ejercicio se obvio que el usuario va a ingresar una lista con elementos_.

Primero realice un filtro en donde solo se pueda continuar si todos los elementos que contiene la lista proporcionada sean del tipo str, si esto no ocurre se le notificará al usuario.
Este ejercicio se soluciono utilizando dos ciclos, en donde el primero recorre todos los elementos de la lista y el segundo recorre los elementos consecutivos al del ciclo anterior, en este ciclo es donde se realiza una comparación haciendo uso de la función sorted que permite organizar strings alfabéticamente, si la palabra del primer ciclo ya organizada es igual (que tiene los mismos caracteres) a cualquiera de las palabras de segundo ciclo, se añaden en pareja dentro de una lista y se guardan dentro otra lista llamada Final_list, en caso de que Final_list este vacio se informara al usuario que no se encontraron anagramas dentro de su lista y se retornará "_None_", sino, se le informará de los anagramas encontradosy se devolvera la lista con dichos anagramas.
