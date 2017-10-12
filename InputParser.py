import string

def inputParser():
    word=''
    inArr=[]
    inString=raw_input('\ninput: ').strip()    

    if len(inString)==0:
        return 0
        
    if inString=='history':
        return inString
    if inString=='clear':
        return inString

    if inString[:5]=='sqrt(':
        inArr=['sqrt(']
        inString=inString[5:]
    
    if inString.find('rt(')!=-1:
        if inString.find('~')!=-1:
            return('invalid input')
        inString=inString.replace(')','')
        inString=inString.replace('rt(', '~')

    inString=inString.replace('pi()',"3.141592653589793")
    inString=inString.replace('e()',"2.718281828459045")
    for char in inString:
        if char.isdigit() or char=='.':
            word+=char
        elif char.isdigit()==False:
            if char.isalpha():
                return('invalid input')
            try:
                inArr+=[float(word)]
            except:
                pass
            word=''
            inArr+=[char]
    try:
        inArr+=[float(word)]
    except:
        None #None for fact to work
        
    #test for //
    for i in range(len(inArr)-1):
        if inArr[i]=='/' and inArr[i+1]=='/':
            inArr[i]='//'
            inArr[i+1]='//'
            inArr=inArr[:i]+inArr[i+1:]
    if inArr[0]=='-':
        inArr[1]*=-1
        inArr=inArr[1:]
        
    #test for negative numbers
    for i in range(2,len(inArr)-1):
        if inArr[i]=='-':
            if type(inArr[i-1]) is str and type(inArr[i+1]) is float:
                inArr[i+1]*=-1
                inArr=inArr[:i]+inArr[i+1:]
    #test for double characters
    for i in range(len(inArr)-1):
        if type(inArr[i])!=float and type(inArr[i+1])!=float:
            return("invalid input")
            
    #don't allow more than 2 numbers and an operation
    if len(inArr)>3:
        return("invalid input") 
        
    #return array of inputs
    return(inArr)
#print(inputParser())
