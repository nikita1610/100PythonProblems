def printparentheses(left, right, out):
  if right==0:
    return
 
  elif left==0:
    print(out+right*")")
 
  elif left==right:
    printparentheses(left-1, right, out+"(")
 
  else:
    printparentheses(left-1, right, out+"(") 
    printparentheses(left, right-1, out+")") 
 
 

def validPar(n):
  printparentheses(n,n,"")
 
 
validPar(4)

    
