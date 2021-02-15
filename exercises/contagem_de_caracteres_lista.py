def contar_caracteres(s):
    """
    FUNÇÃO QUE CONTA OS CARACTERES DE UMA STRING
    :param s: string a ser contada
    """
    num_of_caracteres = {}
    for caracter in s:
        num_of_caracteres[caracter] = (num_of_caracteres.get(caracter, 0) + 1)
    return num_of_caracteres
