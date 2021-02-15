def myatoi(sentence: str):
    """
    This function aims to pass a str type to int type, like (C / C++)'s atoi function
    Time complexity
    Running time O(n)
    Memory Usage O(n)

    :param sentence: str
    :return: int
    """
    find_number = False
    find_less_sign = False
    find_pos_sign = False
    new_sentence = ""
    for letter in sentence:
        if letter == ' ':
            if find_number or find_less_sign or find_pos_sign:
                break
            else:
                pass
        elif letter.isdigit() or letter == "-" or letter == "+":
            if letter == "+":
                if find_number or find_less_sign or find_pos_sign:
                    break
                else:
                    find_pos_sign = True
                    pass
            elif letter == "-":
                if find_number or find_less_sign or find_pos_sign:
                    break
                else:
                    find_less_sign = True
                    pass
            else:
                find_number = True
                new_sentence += letter
        else:
            break
    if new_sentence.isdigit():
        if len(new_sentence) == 0:
            return 0
        elif find_less_sign:
            new_sentence = int(new_sentence)
            return (-2**31) if ((new_sentence * -1) < (-2**31)) else (new_sentence * -1)
        else:
            new_sentence = int(new_sentence)
            return ((2**31) - 1) if (new_sentence > ((2**31) - 1)) else new_sentence
    return 0


# some test cases
if __name__ == "__main__":
    print(myatoi("    +11191657170"))
    print(myatoi("3.14159"))
    print(myatoi("      -11919730356x"))
    print(myatoi(" ++1"))
    print(myatoi("  +  413"))
    print(myatoi("   +0 123"))
    print(myatoi(" "))
    print(myatoi("00000-42a1234"))
    print(myatoi("+"))
    print(myatoi("-1-"))
    print(myatoi("+1"))
    print(myatoi("-"))
    print(myatoi("  w -2www"))
    print(myatoi("   -42"))
    print(myatoi("4193 with words"))
    print(myatoi("words and 987"))
    print(myatoi("-91283472332"))
