def inputParser():
    word=''
    inString=[]
    string=raw_input('\ninput: ').strip()
    for char in string:
        if char.isdigit() or char=='.':
            word+=char
        elif char.isdigit()==False:
            if char.isalpha():
                return('invalid input character')
            try:
                print(word)
                if word.isdigit():
                    inString+=[float(word)]
            except:
                return('invalid input')
            word=''
            inString+=[char]
    try:
        inString+=[float(word)]
    except:
        None #None for fact to work
    for i in range(len(inString)-1):
        if inString[i]=='/' and inString[i+1]=='/':
            inString[i]='//'
            inString[i+1]='//'
            inString=inString[:i]+inString[i+1:]
    return(inString)
