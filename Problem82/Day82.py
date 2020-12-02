def count_words(s,k):
	s=s+" "
	n=len(s)
	w=""
	for item in s:
		if item!=" ":
			w=w+item
		else:
			if len(w)>=k:
				print(w)
			w=""
s="hello! how are you doing ?"
k=4
count_words(s,k)

