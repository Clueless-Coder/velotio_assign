# your code goes here
##assignment 2
def isAnagram(str1,str2):
	if len(str1)!= len(str2):
		return 0
	
	arrset1=set(str1)
	arrset2=set(str2)
	
	if arrset1.issubset(arrset2):
		return 1
	return 0
	
##main
str1='abcd'
str2='badc'
if isAnagram(str1,str2):
	print("Strings are anagrams")
else:
	print("Strings are not anagrams")