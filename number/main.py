"""
Se tiene un arreglo myArray que contiene bloques de números. Los bloques pueden ser de cualquier largo, los números contenidos están en el rango de 1 a 9 y se separan por un cero para definir los bloques. Se deben ordenar los números de los bloques individualmente de menor a mayor e imprimir las secuencias separando los bloques por un espacio. Por ejemplo, para el arreglo: (1,3,2,0,7,8,1,3,0,6,7,1) la respuesta esperada es: 
123 1378 167 
El arreglo y su longitud están definidos en la sección de código predefinido. Asumir que este código predefinido puede variar (valores y longitud del arreglo) y se debe tener en cuenta lo siguiente al programar: 
- El número de bloques es variable. 
- Un cero marca el final de un bloque y el inicio de otro. El inicio del arreglo se asume como el inicio de un bloque y el final de un arreglo se asume como el final de un bloque (Por lo tanto un cero al inicio o al final del arreglo de hecho implicarían un bloque sin elementos)
- Un bloque puede no contener elementos, en cuyo caso se imprimirá una x. Por ejemplo, para (2,1,0,0,3,4) se imprimiría. 
12 X 34 

"""

myArray = (0,1, 3, 2, 0,0,0, 7, 8, 1, 3, 0, 6, 7, 1)
myArrayLength = len(myArray)

def process_blocks(array):
    blocks = []
    current_block = []

    for number in array:
        if number == 0:
            if current_block:  # Si hay números en el bloque actual, lo agregamos
                blocks.append(sorted(current_block))
                current_block = []  # Reiniciamos el bloque actual
            else:
                blocks.append(["X"])  # Agregamos un bloque vacío
        else:
            current_block.append(number)

    # Agregar el último bloque si no está vacío
    if current_block:
        blocks.append(sorted(current_block))
    else:
        blocks.append(["X"])

    return blocks

print(process_blocks(myArray))