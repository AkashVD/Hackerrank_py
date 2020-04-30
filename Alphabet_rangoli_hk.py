#You are given an integer, N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

#N = int(input()) 
#for i in range(N) :
#    print(chr(97+N-i), end = "-")


#pattern = [chr(96+N-i) for i in range(N-1)]  
#mid_pat = "-".join(pattern + [chr(97)] + pattern[::-1])
#w = len(mid_pat)

#top_pat = "-".join(pattern+pattern[::-1])
#print(top_pat)

#Top part
#for i in range(N-1) :
#    print((top_pat[:i]).center(w,"-"))

#Middle part
#print(mid_pat)

#Bottom part
#for i in range(N-1) :
#    print(chr(98+i).center(w, "-"))
import string
ascii = string.ascii_lowercase
#print(ascii)

N = int(input())

pattern = []

for i in range(N):
    s = "-".join(ascii[i:N])
    print(s)
    pattern.append(s[::-1] + s[1:])
    print(pattern)

w = len(pattern[0])
print(w)

for i in range(N-1,0,-1):
    print(pattern[i].center(w,"-"))
    
for i in range(N):
    print(pattern[i].center(w,"-"))    