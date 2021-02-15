def reverse_num(x: int) -> int :
    if x == 0:
        return 0
    else:
        num_temp = str(x)
        tam = len(num_temp)
        num_zeros = 0
        if num_temp[0] == "-":
            if num_temp[tam - 1] == "0":
                dici = {"0": 0}
                for value in num_temp[:1:-1]:
                    if value in dici:
                        dici[value] += 1
                        num_zeros += 1
                    else:
                        break
                num_temp = num_temp[tam-num_zeros:0:-1]
                x = (int(num_temp)) * -1
            else:
                num_temp = num_temp[:0:-1]
                x = (int(num_temp)) * -1
        else:
            if num_temp[tam - 1] == "0":
                dici = {"0": 0}
                for value in num_temp[::-1]:
                    if value in dici:
                        dici[value] += 1
                        num_zeros += 1
                    else:
                        break
                num_temp = num_temp[tam-num_zeros::-1]
                x = (int(num_temp))
            else:
                x = int(num_temp[::-1])
    if x > (2 ** 31 - 1) or x < (-2 ** 31):
        return 0
    else:
        return x


if __name__ == "__main__":
    print(reverse_num(65090))