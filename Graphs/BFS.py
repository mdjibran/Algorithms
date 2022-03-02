def bfs(arr: dict, source:str) -> list:
    q = [ source ]

    while q:
        el = q.pop(0)
        print(el)
        for e in arr[el]:
            q.append(e)



arr = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],

}
print(bfs(arr, 'a'))