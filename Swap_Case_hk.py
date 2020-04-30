#  You are given a string and your task is to swap cases.
#  In other words, convert all lowercase letters to uppercase letters and vice versa.

S = input()
let = []
for i in S :
    if i.islower() :
        let.append(i.upper())
        #print(i.upper(), end = "")
    elif i.isupper() :
        let.append(i.lower())
        #print(i.lower(), end = "")
    else : let.append(i)       

print("".join(let))     