from typing import List
"""
arr = [["s", "", "w", "", "h"],
       ["t", "p", "a", "c", ""],
       ["o", "", "t", "", ""]]

arr = [["s", "", "", "t"],
       ["t", "", "a", "c"],
       ["o", "w", "", "h"],
       ["p", "", "", ""]]
"""


def teste(arr: List[List[str]]):
    i = j = 0
    invert = 0
    result = ""
    while True:
        if invert == 0:
            if arr[i][j] == "":
                return result
            result += arr[i][j]
            i += 1
            if i >= len(arr)-1:
                result += arr[i][j]
                invert = 1
                i -= 1
        if invert == 1:
            j += 1
            result += arr[i][j]
            if i == 0:
                invert = 0
                i += 1
            else:
                i -= 1


def teste_2(arr: List[List[str]]):
    if arr.__len__() == 0:
        return ""
    else:
        i = j = invert = 0
        result = ""
        while True:
            if invert == 0:
                result += arr[i][j]
                i += 1
                if i >= len(arr)-1:
                    result += arr[i][j]
                    invert = 1
                    i -= 1
                    j += 1
                    if i >= len(arr) or j >= len(arr[0]):
                        return result
                    result += arr[i][j]
            if invert == 1:
                if i == 0:
                    invert = 0
                    i += 1
                else:
                    if len(arr) % 2 == 0:
                        j += 1
                        i -= 1
                        result += arr[i][j]
                    else:
                        i -= 1


print()
print(teste_2([["s", "", "", "t"],
             ["t", "", "a", "c"],
             ["o", "w", "", "h"],
             ["p", "", "", ""]]))
print(teste([["s", "o", "w", "t", "h"],
               ["t", "p", "a", "c", ""]]))