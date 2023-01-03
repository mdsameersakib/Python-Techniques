# The eval() function evaluates whatever is inside it..
x = 5
print(eval("x+1+x**2+x**3"))
# gives the output as:
156 
# NB whatever we put inside eval should be a string otherwise it won't work...
