#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be N X M . ( N is an odd natural number, and M is 3 times N .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.


#n, m = map(int,input().split())
#pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
#print(pattern)
#print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
N = int(input())
M = int(input())

for i in range(N//2) :
    print((".|."*(2*i+1)).center(M,"-"))

print("WELCOME".center(M,"-")) 

for i in range(N//2) :
    print((".|."*(N-(2*(i+1)))).center(M,"-"))