def getCordinates(x, y):
    x_val = 1
    inc = 2
    for i in range(1, x):
        x_val += inc
        inc += 1
    
    inc = x
    for i in range(1, y):
        x_val += inc
        inc += 1

    return str(x_val)

print(getCordinates(5,10))


'''
2 = 3
3 = 4

16
11 17 
7  12 18 
4  8  13 19
2  5  9  14  20
1  3  6  10  15  21



col = 1 (0), 2 (3), 3(4), 4(5), 5(6)
row = 1 (0), 2 (2), 3(5), 4(9), 5(14), 6(20)


col * col_dist + row * row_dist

[3,2]
3(3+1) + 2(2+1)
=3(4) + 2 (3)
= 12 + 6
= 18



[1,1]
1(1+1) + 1(1+1)
=1(2) + 1(2)
=2+2


[2,3]
2(2+1) + 3(3+1)
=2(3) + 3(4)
=6+12
=18



'''