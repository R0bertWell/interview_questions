def longest_palindromic(s: str):
    """
    brute force
    index by index
    O ( n² )
    :param s:
    :return:
    """
    i = j = init = 0
    palind = ""
    while i < len(s) - 1:
        arm = s[i:j+2]
        if arm == arm[::-1]:
            if len(arm) >= len(palind):
                palind = arm
        if j == len(s)-1:
            init += 1
            i += 1
            j = init
        j += 1
    return palind
