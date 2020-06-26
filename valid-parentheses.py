def solution(s):
    start = '([{'
    close = ')]}'
    stack = []

    for ch in s:
        if ch in start:
            stack.append(ch)
        elif ch in close:
            if not stack:
                return False
            if start.index(stack.pop()) != close.index(ch):
                return False 
            
    return len(stack) == 0 
        