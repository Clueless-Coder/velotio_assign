# your code goes here
##Assignment 1
arr = list(input())
mx = count=0

for par in arr:
	if par =='(':
		count+=1
		mx=max(mx,count)
	
	if par ==')':
		count-=1

if count!=0:
	print("-1")
else:
	print(mx)