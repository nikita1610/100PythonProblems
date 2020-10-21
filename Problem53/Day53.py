def is_overlapping(a,b):
  if a[0] < b[0] and b[0] < a[1]:
    return True
  else:
    False

def merged_overlap(arr,n):
  arr.sort(key=lambda x: x[0])
  merged_list=[]
  merged_list.append(arr[0])
  for i in range(1, n):
    element=merged_list.pop()
    if is_overlapping(element,arr[i]):
      new_element= [element[0],max(element[1],arr[i][1])]
      merged_list.append(new_element)
    else:
      merged_list.append(element)
      merged_list.append(arr[i])

  return merged_list


l=[[1,3],[2,6],[8,10]]
n=len(l)
m=merged_overlap(l,n)
print(m)
