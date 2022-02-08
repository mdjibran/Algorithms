import sys

def FindDistance(paragraph: list[str]):
    dict = {}
    leastDistance = sys.maxsize

    for i, w in enumerate(paragraph):
        print(i)
        if w in dict:
            leastDistance = min(leastDistance, i- dict[w])


        dict[w] = i
    return leastDistance






print(FindDistance(["All", "no","kill","damn","lol","no"]))

