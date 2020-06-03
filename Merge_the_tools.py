#Input : AABCAAADA
#		 3

#Output : AB
#		  CA
#		  AD

string = "AABCAAADA" #input("String :")
k = 3            #int(input("K :"))

l = len(string)//k
#st = 0
#for i in range(l) :

#MY METHOD-------------------------------

#for i in range(0, len(s), l) :
#	sub = []
#	for j in range(l) :
#		if s[j+i] not in sub :
#			sub.append(s[j+i])
		
#	print("".join(sub))		

#-----------------------------------------	

#OPTIMIZED METHOD-------------------------

temp = []
temp_len = 0
for S in string :
	temp_len += 1
	if S not in temp :
		temp.append(S)
	if temp_len == l :
		print("".join(temp))
		temp = []
		temp_len = 0 	

	
