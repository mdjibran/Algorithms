import string


def StringToInt(stringNum: string):
    d = { '1': 1, 
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9, 
          '0': 0}
    result = 0
    place = 1
    for i in stringNum[::-1]:
        if i == '-':
            result = result * -1
        elif i == '.':
            result = result * 0.1
            place = 1
        else:
            result += d[i] * place
            place *= 10

    return result



print(StringToInt("-12323.005"))
