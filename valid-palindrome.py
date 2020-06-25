import re
def solution(s):
  """
  Input: "A man, a plan, a canal: Panama"
  Output: true
  
  we gotta remove/not consider anything except alphabet and number

  1-we could get use Regex to sub them with ''
  2-two pointer to hop over them if they are not aplanum
  """

  def _regex(s):
    text = re.sub('[^a-zA-Z0-9]','',s)
    
    for i in range(len(text)):
      if text[i].lower() != text[~i].lower():
        return False 

    return True

  def _pointers(s):
    i = 0 
    j = len(s) - 1
    
    while i < j :
      #skip anything not alphanum from the left and right
      #still have to check boundary
      while i < j and not s[i].isalnum():
        i += 1
      while i < j and not s[j].isalnum():
        j -=1

      if i < j and s[i].tolower() != s[j].tolower():
        return False 
    return True
