#You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

#Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

#The possible return strings are: "addition", "subtraction", "multiplication", "division".

#behaviour driven development
#input:user enters values a,b,res as 5,2,7 respectively
#output: function returns addition

#Display subtraction
#INPUT:user enters values a,b,res as 5,2,3 respectively
#OUTPUT:function returns subtraction


#display multiplication
#INPUT:user enters values a,b,res as 5,2,10 respectivly
#OUTPUT: function returns multiplication

#Display division
#INPUT:user enters values a,b,res as 5,2,2.5 respectivly
#OUTPUT: function returns division



#Display a and b dont result to res
#INPUT:user enters values a,b,res as 5,2,1 respectivly
#OUtPUT:function returns a and b dont result to res

#INPUT:user enters values a,b,res as 5, 6 respectivly
#OUTPUT: TypeError: calc_type() missing 1 required positional argument: 'res'


 
#pseudocode
#1. define calc_type
# 2. if condition on argument as per instruction in which return the either(string: addition, subtraction, multiplication, division)
#4. print the strng n degard to the output
def calc_type():

   a=input("enter a number:")
   b=input("enter a number:")
   res=input("enter a number:")
   if a + b == res:
        return "addition"
   elif a-b == res:
        return "subtraction"
   elif a * b == res:
        return "multiplication"
   elif a / b == res:
        return "division"    
   else:
        print (f' {a} and {b} dont result to {res} ') 

calc_type()


