def CheckpathBFS(arr: dict, src:str, dst: str) -> bool:
    q = [src]

    while q:
        el = q.pop(0)
        if el == dst: return True

        for e in arr[el]:
            q.append(e)
    return False



def CheckpathDFS(arr: dict, src: str, dst: str) -> bool:
    if src == dst: return True

    for el in arr[src]:
        if CheckpathDFS(arr, el, dst): return True

    return False




arr = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(CheckpathDFS(arr, 'f', 'k')) 
print(CheckpathBFS(arr, 'f', 'k')) 