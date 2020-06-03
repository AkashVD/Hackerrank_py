#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def line_split_join(line) :
	words = line.split()
	return "-".join(words)

line = input()
result = line_split_join(line)
print(result)	
