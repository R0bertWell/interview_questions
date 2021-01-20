def length_of_longest_substring(s):
    dici = {}
    max_s_rep = repeticao_na_fila = 0
    for i, value in enumerate(s):
        if value in dici:
            num_repetidos = dici[value] + 1
            if num_repetidos > repeticao_na_fila:
                repeticao_na_fila = num_repetidos
        num_repeticoes = i + 1 - repeticao_na_fila
        if num_repeticoes > max_s_rep:
            max_s_rep = num_repeticoes
        dici[value] = i
    return max_s_rep
