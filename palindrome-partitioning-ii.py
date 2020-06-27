def solution(s):
    """
    we want find the minCut to get all valid palidrome substrings:
    
    -We could find all possible list of the palidrome substring and just get the lowest count of the length. => 2^n , we get all the combinations
    
    -Better solution to store all the boolean value for cell with index i,j represent the substring. True for palindrome, False by default
    
    -"aab" 2 possible ways: ['a','a','b'] and ['aa',b]
    if we look into at the string, from the start to the end, we want to count the longest palidromic substring only. 
    - we want to look the from right and iterate from the start up to the right since we want to scan to get the largest substring such we get less cuts
    - [0----j---i-----n]
    if cell[j][i] = true then substring is palindromic
        if j == 0, [0----j----i] should be counted as 1 even when j getting closer, [j--i] might be valid, but we keep the minimum value. 
        always cuts[i] = 0, since it is a palindome from the start
        
        else:
        we know that to have to compare the current count vs previous valid substring + 1, we want to start incement the cut from previous valid substring
        cut[i] = min(cut[i], cut[j-1] + 1) j-1 is the previous valid cut, 
        -when 'aac', at c j == i , will be [j-1] + 1 = 1
    
    """
    
    n = len(s)
    # store boolean for valid substring
    dp = [[False for _ in range(n)] for _ in range(n)]
    # min cuts up to i index
    cuts = [0] * n
    
    for i in range(n):
        # the max count for each char is a palidrome substring by default
        cuts[i] = i
        # i < n
        # j <= i < n that we need i+1 upper bound to let j reach n-1
        for j in range(i+1):
            if j == i:
                dp[j][i] = True
            if s[j] == s[i]:
                dp[j][i] = True if i - j < 2 else dp[j+1][i-1] # check inner substring
                
            if dp[j][i]:
                if j == 0:
                    cuts[i] = 0 # why ? it is a palindrome from the start at index 0 up to i so we count as 1
                else:
                    cuts[i] = min(cuts[i], cuts[j-1] + 1) # index j-1 is the previous valid substring, we will increment from that count by 1 since it is a new valid substring
  
    return cuts[n-1]
    

    