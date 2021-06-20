
t = int(input())
for i in range(t):
	x,y,a,b = map(int, input().split())
	if (y-x) % (a+b) == 0:
		print( int((y-x)/(a+b)) )
	else:
		print(-1)

