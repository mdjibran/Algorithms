def intToRoman(num):
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundereds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']

    return thousands[(num // 1000)] + hundereds[(num%1000)// 100] + tens[(num % 100)//10] + units[num%10]



print(intToRoman(int(3125)))
