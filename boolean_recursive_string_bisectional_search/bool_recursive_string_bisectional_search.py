# determine if a character is in a string, so long as the string is sorted in alphabetical order. 

def isIn(char, aStr):

   if not aStr:
     return False
   index=len(aStr)//2
   
   if len(aStr) == 1:  
       return char == aStr
 
   if char == aStr[index]:
       return True
       
   elif char < aStr[index] :
       return isIn(char,aStr[:index])
   else:
       return isIn(char,aStr[index:])
