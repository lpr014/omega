word=""
inString=[]
string=raw_input('input: ')
for char in string:
	if not char.isdigit():
		inString+=[word]
		word=""
		inString+=[char]
	else:
		word+=char
inString+=[word]
for term in inString:
	if term.isalpha():
		return -1
print(inString)
