def generate_paren(n):
  """
  we want to generate all possible valid parent
  we need to keep track of opening and unclosed paren
  n = 2
  '(' avail opening = 1, unclosed = 1
  '((' avail opening = 0, unclosed = 0

  -case avail opening = 0, we should add all the unclosed ')'
  -case unclosed = 0, that we need an opening inorder to close
  -case avail not 0, we have two options which adding another '('
  and ')' the opening n = 2, '(' => '((' , '()'

  runtime: O(2^2n) = O(2^n) 
  1. at each call of helper we branch off  up to 2 times by adding '(' and ')'
  2. then we go down at a depth of at most 2n, since 2n = # of '(' + # of ')' 
  ==> (branch ^ depth) 2^2n

  space: O(2*n) = O(n) space in recursively stack call of n paren, but we call recursively on ')'
  opening + closing = 2n, O(n)
  """

def helper(cur, num_avail, num_unclosed):
  # base case
  if num_avail == 0:
    # we need to close
    return [cur + ')' * num_unclosed]
  elif num_unclosed == 0:
    # we have an opening that is not closed
    # '(()' , '()('
    return helper(cur + '(', num_avail - 1, num_unclosed + 1)
  else:
    return helper(cur + '(', num_avail - 1, num_unclosed +1 ) + helper( cur + ')' , num_avail , num_unclosed - 1)

