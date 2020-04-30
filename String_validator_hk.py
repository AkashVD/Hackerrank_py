#String Validator
string = input()
alnum = False
alpha = False
dig = False
num = False
upp = False
low = False

for s in string :
    if s.isalnum() :
        alnum = True
    if s.isalpha() :
        alpha = True
    if s.isdigit() :
        dig = True
    if s.isnumeric() :
        num = True
    if s.isupper() :
        upp = True
    if s.islower() :
        low = True 

print(alnum)
print(alpha)
print(dig)
print(num)
print(low)
print(upp)    