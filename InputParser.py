def inputParser():
    word=''
    inString=[]
    string=raw_input('\ninput: ').strip()
    #TESTING
    if string=='history':
        return string
    #TESTING

    if len(string)==0:
        exit()
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
                #add check for length of word and add a return('invalid input') to except
                #test for errors like ++
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
    return(inString)
