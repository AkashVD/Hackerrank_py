def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-(len(sub_string)-1)):
        found = -1
        found = string.find(sub_string)
        print(found)
        #print("Before loop ", string)
        if(found != -1) : 
            count = count + 1
            l = list(string)
            l[found] = "*"
            string = ''.join(l) 
            #print(count)
        else :
            continue 
        #print("After loop ", string)   
    return count 


string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)