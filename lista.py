import random

my_randoms=[]

for i in range (30):
	my_randoms.append(random.randrange(-30,30))

print (my_randoms)
sum=0
	
for i in range(28):
	for j in range(i+1,29):
		for k in range(j+1,30):
			if (my_randoms[i]+ my_randoms[j] + my_randoms[k])==0:
				sum=sum+1
				print (my_randoms[i],my_randoms[j],my_randoms[k])

if sum!=0:				 
        print "Triple combinations having a sum equal to 0 are total %d" %(sum)
else :
                print "No combination has sum=0"
