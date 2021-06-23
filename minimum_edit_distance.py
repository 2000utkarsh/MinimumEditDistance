
import pandas as pd



def ExportToCSV(dp, m , n):
	
	df = pd.DataFrame.from_records(dp)
	df.to_csv('result/test.csv', index=False)

def PrintMatrix(dp, str1, str2,m , n):
	
	
	new_dp = [[0 for x in range(n + 2)] for x in range(m + 2)]
	for i in range(0, m + 1):
		for j in range(1, n + 2):
				new_dp[i][j] = dp[m-i][j-1]

	for i in range(len(str1)):
		new_dp[i][0] = str1[len(str1)-i-1]

	for i in range(len(str2)):
		new_dp[m+1][i+2] = str2[i]
	
	new_dp[m+1][0] = '#'
	new_dp[m+1][1] = '#'
	new_dp[m][0] = '#'

	ExportToCSV(new_dp, m ,n)

def editDistDPLevenshtein(str1, str2, m, n):
	
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
	
	for i in range(m + 1):
		for j in range(n + 1):
			
			if i == 0:
				dp[i][j] = j 

			elif j == 0:
				dp[i][j] = i 
			
			else:
				if str1[i-1] == str2[j-1]:
					
					add = 0
				else:
					add = 2
				dp[i][j] = min(dp[i][j-1]+1,	 
								dp[i-1][j]+1,	 
								dp[i-1][j-1]+add) 

	PrintMatrix(dp,str1, str2, m ,n)
	return dp[m][n]

def editDistDPMinEdit(str1, str2, m, n):
	
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	
	
	for i in range(m + 1):
		for j in range(n + 1):
 
			
			
			if i == 0:
				dp[i][j] = j    
						
			elif j == 0:
				dp[i][j] = i    
 
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
 
			else:
				dp[i][j] = 1 + min(dp[i][j-1],        
								   dp[i-1][j],        
								   dp[i-1][j-1])    

	PrintMatrix(dp,str1, str2, m ,n)
	return dp[m][n]

def editDistDPWeighted(str1, str2, m, n):
	
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	
	
	for i in range(m + 1):
		for j in range(n + 1):
			
			if i == 0:
				dp[i][j] = j 
			
			elif j == 0:
				dp[i][j] = i 

			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			
			else:
				dp[i][j] = 1 + min(dp[i][j-1],	 
								dp[i-1][j],	 
								dp[i-1][j-1]) 
	PrintMatrix(dp,str1, str2, m ,n)
	return dp[m][n]

while True:
	print('\n')
	print("Enter 1 for Mininum Edit Distance")
	print("Enter 2 for Levenshtein Distance")
	print("Press e to exit the program Levenshtein Distance")

	choice = input("Enter your choice: ")
	if choice == 'e' or choice == 'E':
		break

	str1 = input("Enter String 1: ")
	str2 = input("Enter String 2: ")

	
	if choice == '1':
		print("Minimum Edit Distance: ", editDistDPMinEdit(str1, str2, len(str1), len(str2)))
	
	if choice == '2':
		print("Minimum Levenshtein Distance: ", editDistDPLevenshtein(str1, str2, len(str1), len(str2)))
