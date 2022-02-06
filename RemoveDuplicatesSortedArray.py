def RemoveDuplicates(lst: list[int]):
    last_index = 1

    for i in range(1, len(lst)):
        if lst[last_index - 1] != lst[i]:
            lst[last_index] = lst[i]
            last_index += 1

    return lst[:last_index]


print(RemoveDuplicates([2,3,5,5,7,11,11,13]))

