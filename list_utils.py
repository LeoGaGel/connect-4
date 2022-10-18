# Funciones para:
# 1. Detectaremos la presencia de UNA instancia del elemento dentro de una lista, en cualquier posición.
# 2. Detectaremos la presencia de N instancias dentro de una lista, en cualquier posición
# 3. Detectaremos la presencia de N elementos SEGUIDOS dentro de una lista.

def find_one(list, needle):
    """
    Devuelve True si encuentra a needle en la lista en alguna posición
    Sino, devuelve False
    """
    return find_n(list, needle, 1)

def find_n(list, needle, n):

    if n > 0:
        # inicializo el contador de veces que lo he encontrado
        # inicializo el indice del elemento actual
        index = 0
        count = 0
        # mientras no haya encontrado n veces y no haya terminado la lista
        while count < n and index < len(list):
            # si la encuento, actualizo el contador 
            if needle == list[index]:
                count = count + 1

            #pase lo que pase, actualizo el contador
            index = index + 1
        
        # devuelvo el resultado de comparar n con el contador
        return count >= n
    else:
        # pregunta idiota
        return False

def find_streak(list, element, size):
    """
    Devuelve True si en list hay size o más elementos SEGUIDOS  
    False en caso contrario y también si size <= 0
    """
    if size > 0:
        # Inicializo el indice, el contador, y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya ecnontrado a size elements seguidos y la lista no se haya terminado
        while count < size and index < len(list):
            
            if list[index] == element:
                # si lo encuentro, activo el indicador de rachas y incremento el contador
                streak = True
                count = count + 1
            else:
                # si no lo encuentro, desactivo indicador de rachas y pongo contador a cero
                streak = False
                count = 0
            
            # avanzo al siguiente elemento (incremento indice)
            index = index + 1
        
        # devolvemos el resultado de comparar el contador con size, 
        # SIEMPRE Y CUANDO ESTEMOS EN RACHA
        if streak == True:
            return count >= size
        else:
            return False       
    else:
        return False

def first_elements(list_of_list):
    """
    Recibe una lista de listas y devuelve una 
    lista con los primeros elementos de la original
    """
    return nth_elements(list_of_list, 0)

def nth_elements(list_of_list, n):
    """    Recibe una lista de listas y devuelve una 
    lista con los xnesimos elementos de la original"""
    result = []
    # mirar como se haría con map
    for list in list_of_list:
        result.append(list[n])
    return result

def transpose(matrix):
    """
    Recibe una matriz y devuelve su transpuesta
    """
    transp = []
    for i in range(len(matrix[0])):
        transp.append(nth_elements(matrix, i))
    return transp

def displace(l, distance, filler = None):
    if distance == 0:
        return l
    elif distance > 0:
        filling = [filler] * distance
        res = filling + l
        res = res[:-distance]
        return res
    elif distance < 0:
        filling = [filler] * abs(distance)
        res = l + filling
        res = res[abs(distance):]
        return res
    
def displace_matrix(matrix):
    # creo una lista vacia que ire construyendo
    d = []
    # por cada columna de la matrix original la desplazo indice -1
    for i in range(len(matrix)):
        # añado la columna desplazada a la matriz que estoy construyendo
        d.append(displace(matrix[i], i -1))
    return d

def replace(elements, predicate, new_value):
    new_list = []
    for element in elements: 
        if predicate(element):
            new_list.append(new_value)
        else:
            new_list.append(element)
    return new_list

def replace_matrix(matrix, predicate, new_element):
    accum = []
    for sublist in matrix:
        accum.append(replace(sublist, predicate, new_element))
    return accum

def reverse_list(l):
    return list(reversed(l))

def reverse_matrix(m):
    accum = []
    for line in m:
        accum.append(reverse_list)
    return accum
