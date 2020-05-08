a = [3,76,2,100,34,21,67,32]

def quickSort(a):
    if len(a) <= 1:
        return a
    pivot = a[int(len(a)/2)]
    short, equal, larger = [], [], []

    for x in a:
        if x < pivot:
            short.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quickSort(short) + equal + quickSort(larger)



print(quickSort(a))
