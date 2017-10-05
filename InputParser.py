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
        inString=['sqrt(']
        string=string[5:]
    
    for char in string:
        if char.isdigit() or char=='.':
            word+=char
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
        
    #test for //
    for i in range(len(inString)-1):
        if inString[i]=='/' and inString[i+1]=='/':
            inString[i]='//'
            inString[i+1]='//'
            inString=inString[:i]+inString[i+1:]
    if inString[0]=='-':
        inString[1]*=-1
        inString=inString[1:]
        
    #test for negative numbers
    for i in range(2,len(inString)-1):
        if inString[i]=='-':
            if type(inString[i-1]) is str and type(inString[i+1]) is float:
                inString[i+1]*=-1
                inString=inString[:i]+inString[i+1:]
    #test for double characters
    for i in range(len(inString)-1):
        if type(inString[i])!=float and type(inString[i+1])!=float:
            return("invalid input")
            
    #don't allow more than 2 numbers and an operation
    if len(inString)>3:
        return("invalid input") 
        
    #return array of inputs
    return(inString)
