def convert_to_zig_zag(s: str, numRows: int):
    """
    Um pouco mais lenta que a de baixo
    """
    arr = [[]]
    i = j = n = 0
    inversion = False
    while j < len(s):
        if numRows > 1:
            if len(arr) < numRows:
                arr += [[]]
            if inversion is False:
                arr[i] += s[j]
                j += 1
                i += 1
                if i >= numRows:
                    i -= 1
                    inversion = True
            else:
                i -= 1
                arr[i] += s[j]
                j += 1
                if i == 0:
                    i += 1
                    inversion = False
        else:
            arr[0] += s[j]
            j += 1
    s = ""
    while n < len(arr):
        s += "".join(arr[n])
        n += 1
    return s


def zig_zag_convert(s: str, numRows: int):
    """
    Um pouco mais rapida que a de cima
    """
    i = j = 0
    string_final = ""
    multi_init = (numRows - 1) * 2
    multi_mid = 0
    if len(s) < 2 or numRows < 2:
        return s
    else:
        while j != numRows:
            if j == 0:
                string_final += s[i::multi_init]
                multi_mid = multi_init - 2
                j += 1
                i += 1
            elif (numRows - 1) > j > 0:
                string_final += s[i:multi_mid + i + 1:multi_mid]
                while multi_init + i < len(s):
                    if i + multi_init < len(s):
                        i += multi_init
                        string_final += s[i:multi_mid + i + 1:multi_mid]
                    else:
                        continue
                i = j + 1
                j += 1
                multi_mid -= 2
            else:
                string_final += s[i::multi_init]
                return string_final
        return string_final
