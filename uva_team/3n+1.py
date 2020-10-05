
def solution(n):
  count = 1
  while n > 1:
    n = ((3*n) + 1) if (n%2 == 1) else (n//2)
    count += 1
  return count

while True:
  try:
    data = input()
    print(data)
    data = [int(x) for x in input().split(" ")]
    ans = 0
    for i in range(data[0], data[1]+1):
      ans = max(solution(i),ans)
    print('{} {} {}'.format(data[0],data[1],ans))
  except EOFError:
    break
  except TypeError:
    print("failed")
    break
  except:
    break
