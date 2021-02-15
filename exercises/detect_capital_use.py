def detect_capital_use(word: str):
    if word.islower() or word.isupper():
        return True
    if word[0].islower() or word[0].isupper():
        return True if word[1:].islower() else False


def detect_capital_use_simplify(word: str):
    return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())


#test cases
if __name__ == "__main__":
    print(detect_capital_use_simplify("aaaaa"))
    print(detect_capital_use_simplify("aaaaA"))
    print(detect_capital_use_simplify("a"))
    print(detect_capital_use("A"))
    print(detect_capital_use("Aaaaa"))
    print(detect_capital_use("AA"))
    print(detect_capital_use("aaaaa"))
    print(detect_capital_use("aa"))
    print(detect_capital_use("AaAaA"))
    print(detect_capital_use("AaaA"))
