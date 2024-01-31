def TowerOfHanoi(n , s, d, t):
	if n==1:
		print ("Move disk 1 from source",s,"to destination",d)
		return
	TowerOfHanoi(n-1, s, t, d)
	print ("Move disk",n,"from source",s,"to destination",d)
	TowerOfHanoi(n-1,t,d,s)
n = int(input("Enter number of disk:"))
TowerOfHanoi(n,'A','B','C') 

