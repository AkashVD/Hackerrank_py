#  Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores.
#  Store them in a list and find the score of the runner-up.

n = int(input())


score = [int(score) for score in input().split()]

#l = max(score)
#print(sorted(score))
#x = list(map(int, input().split()))
#print(x)

large = None
sec_large = -1
for i in score :
    if large is None or i > large :
        sec_large = large
        large = i 

print(large)
print(sec_large)

for i in score :     
    if  i < large and i > sec_large :
        sec_large = i    

print(large)
print(sec_large)