def solution(numerator, denominator):
  """
  we want to find all the fractions will the repeating number and we will apply division algorithm. First result = divisor / dividend, we get the left hand side '.'
  remainder = divisor % dividend
  if remainder is 0 then return the result which is a whole number
  else if remainder is not 0, we follow division algorithm by finding next decimal as follow: 
  -next decimal = (remainder * 10 ) / dividend
  -remainder = (remainder * 10) % dividend (update the remainder til it is zero)
  we keep storing the index of each decimal, when we find the repeating decimal, insert ( and at the end )
  """

  if numerator == 0:
    return '0'

  res = []

  if (numerator > 0) ^ (denominator > 0):
    res.append('-')

  divisor = abs(numerator)
  dividend = abs(denominator)
  n = divisor // dividend
  rem = divisor % dividend
  res.append(str(n))
  
  if rem == 0:
    return ''.join(res)

  hm = {}
  while rem != 0:
    if rem in hm:
      res.insert(hm[res], '(')
      res.append(')')
      break 
      # keep track of the decimal
      hm[rem] = len(res)
      # find next decimal by multiply by 10
      rem *= 10
      n = rem // dividend
      # add into the result
      res.append(str(n))
      # find the next remainder
      rem %=  dividend
  return ''.join(res)
