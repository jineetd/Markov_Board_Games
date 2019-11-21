import numpy as np

#x = input("Enter the number of attacker army : ")
#y = input("Enter the number of defender army : ")
#attackers_army = int(x)
#defenders_army = int(y)

def theoretical_dynamic(attackers_army,defenders_army):
	total_states = (attackers_army+1)*(defenders_army+1)

	absorbing_states = attackers_army + defenders_army + 1

	transition_states = ((attackers_army+1)*(defenders_army+1)) - (attackers_army + defenders_army + 1)

	transition_matrix = [[0.0]*total_states for _ in range(total_states)]

	Q_matrix = [[0.0]*(transition_states) for _ in range(transition_states)]

	R_matrix = [[0.0]*(absorbing_states) for _ in range(transition_states)]

	def matrix_defender_losing(i,j,k):
		while (i>=k and j>=k):
			transition_matrix[i][j] = (float)(15)/36
			i = i-1
			j = j-1


	def matrix_attacker_losing(i,j,k):
		while(i>=k and j>=k):
			transition_matrix[i][j] = (float)(21)/36
			i = i-defenders_army
			j = j-defenders_army

	#for absorbing states
	i=0
	while (i<absorbing_states):
		transition_matrix[i+transition_states][i+transition_states] = 1
		i = i+1

	#for transition to absorbing states
	i=0
	j=transition_states + defenders_army
	while(j>=transition_states and i<=(transition_states-defenders_army)):
		transition_matrix[i][j] = (float)(15/36)
		j = j-1
		i = i+defenders_army

	i=0
	j=total_states - defenders_army
	while(j<=(total_states-1) and i<=(defenders_army-1)):
		transition_matrix[i][j] = (float)(21/36)
		i=i+1
		j=j+1

	#for transition to transition states
	l = defenders_army-1
	while(l<=((defenders_army*attackers_army)-1)):
		matrix_defender_losing(l,l-1,l-(defenders_army-1))
		l = l+defenders_army


	m=0
	while(m<=(defenders_army-1)):
		matrix_attacker_losing(m+(defenders_army*attackers_army)-defenders_army , m + (defenders_army*attackers_army)-(2*defenders_army),m)
		m=m+1


	i=0
	while (i<transition_states):
		j=0
		while(j<transition_states):
			Q_matrix[i][j] = transition_matrix[i][j]
			j = j+1
		i = i+1
	i=0
	while(i<transition_states):
		j=transition_states
		while(j<=(total_states-1)):
			R_matrix[i][j-transition_states] = transition_matrix[i][j]
			j = j+1
		i = i+1
	identity_matrix = np.identity(transition_states)

	subtracted_matrix = np.subtract(identity_matrix , Q_matrix)
	inverse_matrix = np.linalg.inv(subtracted_matrix)
	#multiplied_matrix = np.dot(np.mat(inverse_matrix), np.mat(R_matrix))
	multiplied_matrix = np.matmul(inverse_matrix,R_matrix)
	#prob_for_win_of_attackers = 0
	prob_for_win_of_defenders = 0
	#print(multiplied_matrix.shape)
	#i=0
	#while (i<=attackers_army):
	#	prob_for_win_of_attackers = prob_for_win_of_attackers + multiplied_matrix[transition_states-1][i]
	#	i = i+1
	i=1
	while(i<=defenders_army):
		prob_for_win_of_defenders = prob_for_win_of_defenders + multiplied_matrix[transition_states-1][i+attackers_army]
		i = i+1

	ans = 0
	i=0
	while (i<transition_states):
		ans = ans + inverse_matrix[transition_states-1][i]
		i=i+1

	print("Expected number of battles are : " + str(ans))
	print("Winning probability of attackers : " + str(1-prob_for_win_of_defenders))
	print("Winning probability of defenders : " + str(prob_for_win_of_defenders))
	return ans,1-prob_for_win_of_defenders,prob_for_win_of_defenders

