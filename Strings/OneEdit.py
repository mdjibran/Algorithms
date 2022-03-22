def OneEdit(s1: str, s2: str) -> bool:
    
    isDifferent = False
    for i in range(len(s2)) :
        if s1[i] != s2[i]:
            if(isDifferent):
                return False
            isDifferent = True
        
            
    return True
    




s1 = 'pale'
s2 = 'ple'

print(OneEdit(s1, s2))