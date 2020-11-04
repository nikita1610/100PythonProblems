def max_length(s):
  braces=[]
  list_count=[]
  count=0
  for item in s:
    if item=="{":
      braces.append(item)
    elif braces:
      count+=1
      braces.pop()
    else:
      list_count.append(count)
      count=0
  return max(list_count)*2

s="{}{}}"
print(max_length(s))
