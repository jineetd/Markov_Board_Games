import numpy as np

transition_matrix = [[0]*56 for _ in range(56)]
Q_matrix = [[0]*42 for _ in range(42)]
R_matrix = [[0]*14 for _ in range(42)]

def matrix_defender_losing(i,j,k):
	while (i>=k and j>=k):
		transition_matrix[i][j] = float(15)/36
		i = i-1
		j = j-1

def matrix_attacker_losing(i,j,k):
	while(i>=k and j>=k):
		transition_matrix[i][j] = float(21)/36
		i = i-6
		j = j-6


def theoretical_values():
	
	#for absorbing states
	i=0
	while (i<14):
		transition_matrix[i+42][i+42] = 1
		i = i+1

	#for transition to absorbing states
	i=0
	j=48
	while(j>=42 and i<=36):
		transition_matrix[i][j] = float(15)/36
		j = j-1
		i = i+6

	i=0
	j=50
	while(j<=55 and i<=5):
		transition_matrix[i][j] = float(21)/36
		i=i+1
		j=j+1

	#for transition to transition states
	matrix_defender_losing(5,4,0)
	matrix_defender_losing(11,10,6)
	matrix_defender_losing(17,16,12)
	matrix_defender_losing(23,22,18)
	matrix_defender_losing(29,28,24)
	matrix_defender_losing(35,34,30)
	matrix_defender_losing(41,40,36)

	matrix_attacker_losing(36,30,0)
	matrix_attacker_losing(37,31,1)
	matrix_attacker_losing(38,32,2)
	matrix_attacker_losing(39,33,3)
	matrix_attacker_losing(40,34,4)
	matrix_attacker_losing(41,35,5)

	#print(transition_matrix)
	i=0
	while (i<42):
		j=0
		while(j<42):
			Q_matrix[i][j] = transition_matrix[i][j]
			j = j+1
		i = i+1
	i=0
	while(i<42):
		j=42
		global R_matrix
		while(j<=55):
			R_matrix[i][j-42] = transition_matrix[i][j]
			j = j+1
		i = i+1
	identity_matrix = np.identity(42)

	subtracted_matrix = np.subtract(identity_matrix , Q_matrix)
	inverse_matrix = np.linalg.inv(subtracted_matrix)
	#multiplied_matrix = np.dot(np.mat(inverse_matrix), np.mat(R_matrix))
	#print(inverse_matrix)
	#print(inverse_matrix.shape)
	R_matrix=np.array(R_matrix)
	#print(R_matrix)
	#print(R_matrix.shape)
	multiplied_matrix = np.matmul(inverse_matrix,R_matrix)
	prob_for_win_of_attackers = 0
	prob_for_win_of_defenders = 0
	#print(multiplied_matrix)
	i=0
	while (i<7):
		prob_for_win_of_attackers = prob_for_win_of_attackers + multiplied_matrix[41][i]
		i = i+1
	i=1
	while(i<=6):
		prob_for_win_of_defenders = prob_for_win_of_defenders + multiplied_matrix[41][i+7]
		i = i+1

	ans = 0
	i=0
	while (i<42):
		ans = ans + inverse_matrix[41][i]
		i=i+1

	print(ans)
	print("Winning probability of attackers : " + str(prob_for_win_of_attackers))
	print("Winning probability of defenders : " + str(prob_for_win_of_defenders))
	return ans,prob_for_win_of_attackers,prob_for_win_of_defenders

#print(theoretical_values())