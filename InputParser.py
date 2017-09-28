def inputParser():
	word=""
	inString=[]
	string=raw_input('input: ')
	for char in string:
		if not char.isdigit():
			if char.isalpha():
				return -1
			inString+=[word]
			word=""
			inString+=[char]
		else:
			word+=char
	inString+=[word]
	return(inString)
