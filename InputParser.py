def inputParser():
    word=''
    inString=[]
    string=raw_input('\ninput: ').strip()
    #Changed to fix History output
    if string=='history':
        return string

    if len(string)==0:
        return 0

    if string[:5]=='sqrt(':
        return ['sqrt(',float(string[5:-1]),')']
    
    for char in string:
        if char.isdigit() or char=='.':
            word+=char
            #print("decimal",char)
        elif char.isdigit()==False:
            if char.isalpha():
                return('invalid input')
            try:
                inString+=[float(word)]
            except:
                pass
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
    if inString[0]=='-':
        inString[1]*=-1
        inString=inString[1:]
        
    for i in range(2,len(inString)-1):
        if inString[i]=='-':
            if type(inString[i-1]) is str and type(inString[i+1]) is float:
                inString[i+1]*=-1
                inString=inString[:i]+inString[i+1:]
    
    for i in range(len(inString)-1):
        if type(inString[i])!=float and type(inString[i+1])!=float:
            return("invalid input")
    if len(inString)>2:
        return("invalid input")        
    return(inString)
