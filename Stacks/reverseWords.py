def reverseWords(s: str) -> str:
    word = []
    result = []

    for c in s:
        if c != ' ':
            word.append(c)
        
        elif len(word) > 0:
            result.append(''.join(word))
            word.clear()
    
    if len(word) > 0:
        result.append(''.join(word))
    return ' '.join(result[::-1])






print(reverseWords("Hello World this is an awesome example"))