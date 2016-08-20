A,B=map(int,input().split())

sub=A-B 
if sub%10==9 :
	print(sub-1)
else:
	print(sub+1)