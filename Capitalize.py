#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
#For example, alison heck should be capitalised correctly as Alison Heck.
#Given a full name, your task is to capitalize the name appropriately.

name = input()
#print(name)
L = name.split(" ")
print(L)
for i in range(len(L)):
    L[i] = L[i].capitalize()    
    
s = " ".join(L)
print(s)
    