
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
