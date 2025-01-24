
"""
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples
of num until the list length reaches length."""

def length(num, length):
    multiple=[]
    for i in range(1,length+1):
        multiple.append(num*i)
    return multiple
print(length(7,5))