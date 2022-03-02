# arithmetic operators
# + sum
# - subtraction
# * multiplication
# / division
# ** numerical potential
# %rest
# // integer division
#----------------------------------
# precedence order
# 1  ()
# 2  **
# 3  * / // %
# 4  + -
#----------------------------------
n1 = float(input('type the first number: '))
n2 = float(input('type the second number: '))
s = n1+n2
div = n1/n2
mult = n1*n2
rest = n1%n2
pot = n1**n2
print(' The sum is {}\nThe Division is {}\nThe Multiplication is{}\nThe Rest is {}\nThe potential is {}'.format(s,div,mult,rest,pot))
yknow = float(input('do you know how to do this math?\n3*(n1+n2)//n1**2/10\n\n1 for yes or 2 for no\n'))
result = 6**(n1+n2)/n1**5/10
if (yknow == 1):
    x = input(print('The result is {:.3f}?\nyes our no?'.format(result)))
    if (x =='yes'):
        print('Nice, you is really smart!')
    else:
        print('Do you need to studie :(')
else:
    print('Nice, you are very smart, your result was {:.1f} '.format(result))
