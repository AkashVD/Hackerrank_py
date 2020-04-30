#Text Wrap
#You are given a string S and width w .
#Your task is to wrap the string into a paragraph of width w .
##NT :: textwrap.fill --> wraps the sring into the list of specified width 
##NT :: textwrap.wrap --> wraps the string into the string of specified width

import textwrap

def wrap(string, max_width):
    #print(textwrap.wrap(string, max_width),"\n")
    #print(textwrap.fill(string, max_width))
    return textwrap.fill(string, max_width)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)