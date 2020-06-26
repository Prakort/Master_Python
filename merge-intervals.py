def solution(intervals):
    """
    we want to merge the overlap 
    [s1, e1] [s2, e2]
    in order to check for overlap, we have to make the first value is sorted
    so we know which pair to start, We need sort based on first value

    Fact: list is sorted based on first value => s1 <= s2
    - rule if e1 < s2 => no overlap, add [s2, e2] as a new interval
    - rule if e1 > s2 => overlap BUT we have to check if e1 <= e2, if e1 > e2,
    this breaks the rule, ending time is LESS than start time.
    if e1 > s2 and e1 <= e2 then [s1, e1] := [s1, e2] merge DONE
    - always pick the last element from result to compare the next pair from the intervals
    """
    if not intervals:
        return []
    # sort based on the first index
    intervals.sort(key=lambda x: x[0])

    res = []
    # add the first pair
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        # assign temp, readable
        A = res[-1]
        B = intervals[i]
        # found overlap, and first end <= second end
        if A[1] >= B[0] and A[1] <= B[1]:
            # change the first to second end
            res[-1][1] = B[1]
        elif A[1] < B[0]:
            # no overlap, add into the res
            res.append(B)
            
    return res
