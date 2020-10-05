





data = []
while True:
  try:
    data = [int(x) for x in input().split(' ')]
    print('case #{} : {}'.format(0,data))
  except EOFError:
    break

