#converting imutate string to mutate string
# mutate means changeable 
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    print(l)
    print(type(l))
    string = ''.join(l)
    print(type(string))
    return string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)