from array import array


def dfs(arr: dict, source: str) -> list:
    stack = [source]

    while stack:
        el = stack.pop()
        print(el)
        for e in arr[el]:
            stack.append(e)



arr = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],

}
print(dfs(arr, 'a'))