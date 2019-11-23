import random
def getBattles(n,m):
	attacker=n

	defender=m

	no_of_battles=0

	while (attacker!=0 and defender!=0):
		aturn = random.choice([1,2,3,4,5,6])
		dturn = random.choice([1,2,3,4,5,6])
		if aturn>dturn:
			defender=defender-1
		else:
			attacker=attacker-1
		no_of_battles=no_of_battles+1

	if(attacker==0):
		return no_of_battles,0,1
	else:
		return no_of_battles,1,0


awin=0
dwin=0
ans=0
for i in range(10000):
	num,a,d=getBattles(7,13)
	ans=ans+num
	awin=awin+a
	dwin=dwin+d

print(float(ans)/10000)
print(float(awin)/10000)
print(float(dwin)/10000)