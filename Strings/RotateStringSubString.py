def Rotate(s1, s2):
    if len(s1) != len(s2): return False
    s = [s1, s1]

    isSubstring(''.join(s), s2)
