from typing import List


def valid_number(s: List[List[str]]) -> bool:
    i = 0
    floated = 0
    number = 0
    elevate = 0
    signed = 0
    while i < len(s):
        if i == 0:
            if s[i] == "-" or s[i] == "+":
                signed = 1
                i += 1
                continue
            elif s[i] == ".":
                floated = 1
                i += 1
                continue
            elif s[i].isdigit():
                number = 1
                i += 1
                continue
            else:
                return False
        else:
            if elevate:
                if s[i] == "-" or s[i] == "+":
                    if s[i-1] == "e":
                        i += 1
                        continue
                    else:
                        return False
            else:
                if s[i] == "-" or s[i] == "+":
                    return False
            if s[i].isdigit():
                number = 1
                i += 1
                continue
            elif s[i] == ".":
                if elevate:
                    return False
                else:
                    if floated:
                        return False
                    else:
                        if number:
                            floated = 1
                            i += 1
                            continue
                        else:
                            floated = 1
                            i += 1
                            continue
            elif s[i] == "e" or s[i] == "E":
                if elevate:
                    return False
                else:
                    if not number:
                        return False
                    elif number:
                        elevate = 1
                        i += 1
                        continue
            else:
                return False
    if signed and floated and not number:
        return False
    if elevate:
        if s[-1] == "-" or s[-1] == "+" or s[-1] == "e" or s[-1] == "E":
            return False
        else:
            return True
    if len(s) == 1 and (s[0] == "." or s[0] == "-" or s[0] == "+"):
        return False
    else:
        return True


if __name__ == "__main__":
    lista = ["+e", ".e", "-e", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "-", "+", "."]
    for i in lista:
        print(valid_number(i))
