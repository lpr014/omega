def inputParser():
    word=""
    inString=[]
    string=raw_input('\ninput: ').strip()
    for char in string:
        if char.isdigit() or char==".":
            word+=char
        elif char.isdigit()==False:
            if char.isalpha():
                return('invalid input')
            try:
                inString+=[float(word)]
            except:
                return('invalid input')
            word=''
            inString+=[char]
    try:
        inString+=[float(word)]
    except:
        return('invalid input')
    return(inString)
