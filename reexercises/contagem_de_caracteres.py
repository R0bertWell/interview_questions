def contagem_de_caracteres(s: str):
    dici = {}
    for value in s:
        dici[value] = dici.get(value, 0)+1
    return dici
