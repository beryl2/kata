#Your task is to make two functions (max and min, or maximum and minimum, etc., depending on the language) that receive a list of integers as input and return, respectively, the largest and lowest number in that list.
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
 
def maximum (nums):
  maximum = max(nums)
print("the largest number is ", maximum)    

#Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet(name):
  if name == "jonny":
    return "hello my love!"
  else:

    return "hello, james"