import sys
def main():
	pydict = {}						#Initialize the dictionary
	file = open("dictionary.txt", "r")		#Open file containing the referrence
	print "Solving jumbled word . . . "
	for word in file:					#Loop through each word in the referrence
		word = word.strip().lower()			#Remove newlines and convert to lowercase
		sortword = ''.join(sorted(word))
		if sortword in pydict:				#To check if sortword is already a key
			if word not in pydict[sortword]:	#Make sure word is not already in the list under the key sortword
				pydict[sortword].append(word)	#Append to the list under the key sortword
		else:						
			pydict[sortword] = [word]		#Create a new list with one entry
	jumbled = sys.argv[1]
	jumbled = jumbled.lower()				#Convert input to lower case
	jumbled = ''.join(sorted(jumbled))		#Sort input alphabetically
	if jumbled in pydict:				#If sorted input exists in the reference
		results = pydict[jumbled]			#Get list of words that match jumbled
		for result in results:			#Loop through list storing the results
			print result,			#Here should be a space between entries
		print ""				
	else:						#Input not found in reference
		print "Results for the jumbled word don't exist in the given file"
			
#Standard boilerplate for main
if __name__=='__main__' :
	main()