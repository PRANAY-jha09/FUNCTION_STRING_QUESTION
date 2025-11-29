###DAY 04 : FUNCTION & STRING

#Create a function that takes two numbers and an operator (+, -, *, /) as parameters and returns the result of the operation

def calculate(num1,num2,operator):
    if operator =='+':
        return num1+num2
    elif operator =='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator =='/':
        if num2==0:
            return "Error : division by zero"
        return num1/num2
    else:
        return "Error: Invalid operator"
#example use
print(calculate(10,5,'+'))
print(calculate(10,5,'-'))
print(calculate(10,5,'*'))
print(calculate(10,5,'/'))
print(calculate(10,5,'%'))

#Write a function that takes a string as input and returns True if it's a palindrome,False otherwise
def palidrome_check(text):
    cleaned=text.replace(" " ," ").lower()
    return cleaned==cleaned[::-1]
print(palidrome_check("racecar"))