import os 

alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = [' ', '!', '#', '$', '%', '&', "'", '?', '@' ]

commonpairs = [
	['t', 'h', 'a', 'i', 'e', 'n', 'r', 'e', 'e', 'o', 't', 'h', 'e', 'e', 's', 'n', 'o', 'a', 'h', 'a', 'i', 'n', 'i', 'o', 'e', 'o',
		't', 'a', 't', 's', 'm', 's', 'n', 'w', 'v', 'l', 'n', 't', 'a', 'd', 'o', 's', 'd', 'l', 't', 'e', 'r', 'a', 'd', 'e', 'r', 'r', 's'],
	['h', 'e', 'n', 'n', 'r', 'd', 'e', 'd', 's', 'u', 'o', 'a', 'n', 'a', 't', 't', 'n', 't', 'i', 's', 't', 'g', 's', 'r', 't', 'f',
		'i', 'r', 'e', 'e', 'e', 'a', 'e', 'a', 'e', 'e', 'o', 'a', 'l', 'e', 't', 'o', 't', 'l', 't', 'l', 'o', 'd', 'i', 'w', 'a', 'i', 'h']]

subs = [
	['@', '8', '(', '6', '3', '#', '9', '#', '1', '!', '<', '1', 'i', '0', '9', '5', '$', '+', '>', '<', '%', '?'],
	['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'k', 'l', 'l', 'o', 'q', 's', 's', 't', 'v', 'v', 'x', 'y']]

passwd = "test"

def charcounter(passwd, size, flag, totalcarry):

	length = size;

	totalalpha = 0;
	totalALPHA = 0;
	totalnumber = 0;
	totalsymbol = 0;

	total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	alphacounter = [ 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ALPHAcounter = [ 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	numbercounter = [ 0,0,0,0,0,0,0,0,0,0 ]
	symbolcounter = [0,0,0,0,0,0,0,0,0,0 ]

	#Character Counter_________________________________________________

	for i in range(26):					# Run through all Alphabet lists
		for j in range(length):			# For each letter in the password
			if (passwd[j] == alphabet[i]):
				alphacounter[i] += 1 # Counter for lowercase
				totalalpha += 1

			if (passwd[j] == ALPHABET[i]):
				ALPHAcounter[i] += 1 # Counter for CAPITAL
				totalALPHA += 1

	for  k in range(10):					# Run through all Number/ Symbol lists
		for l in range(length):			# For each letter in the password
			if (passwd[l] == numbers[k]):
				numbercounter[k] += 1 # Counter for numbers 
				totalnumber += 1;

			if (passwd[l] == symbols[k]):
				symbolcounter[k] += 1 #Counter for symbols
				totalsymbol += 1

	# Breakdown readout

	for m in range(26):					# Run through all Alphabet lists
		if (alphacounter[m] >= 1):
			if (flag > 1):
				Log("	Character:	'" + alphabet[m] + "'		Amount: " << alphacounter[m])
			
		if (ALPHAcounter[m] >= 1):
			if (flag > 1):
				Log("	Character:	'" + ALPHABET[m] + "'		Amount: " << ALPHAcounter[m])

	for n in range(10):					# Run through all symbol lists
		if (numbercounter[n] >= 1):
			if (flag > 1):
				Log("	Character:	'" + numbers[n] + "'		Amount: " << numbercounter[n])
			
		if (ALPHAcounter[n] >= 1):
			if (flag > 1):
				Log("	Character:	'" + symbols[n] + "'		Amount: " << symbolcounter[n])


	if (flag >= 1):
		Log("\n	The password consists of in total: \n");

		Log("	Lowercase characters:	" + totalalpha);
		Log("	UPPERCASE characters:	" + totalALPHA);
		Log("	Numbers             :	" + totalnumber);
		Log("	Symbols             :	" + totalsymbol);
	

	# Suggestions and Grade

	if (totalALPHA < 2):
		if (flag >= 1):
			Log("	Your password contains a low amount of uppercase characters!")
		else:
			if (flag > 1):
				LogIn("	Good Amount of uppercase, Entropy + 1")

			total[0] += 1

		if (totalnumber < 2):
			if (flag >= 1):
				Log("	Your password contains a low amount of numbers!")
		else:
			if (flag > 1):
				LogIn("	Good Amount of numbers, Entropy + 1 \n")

			total[0] += 1

		if (totalsymbol < 2):
			if (flag >= 1):
				Log("	Your password contains a low amount of symbols! \n")
		
		else:
			if (flag > 1):
				LogIn("	Good Amount of symbols, Entropy + 1 \n")
			
			total[0] += 1;

		if (totalalpha > 10):
			if (flag >= 1):
				Log("	Your password contains a lot of lowercase! \n")
		
		else:
			if (flag > 1):
				LogIn("	Good Amount of lowercase, Entropy + 1 \n")
			total[0] += 1;

	return total;

def lengthcounter(size, flag, totalcarry):

	total[3];
	total[0] = totalcarry[0]
	total[1] = totalcarry[1]
	total[2] = totalcarry[2]

	if (flag >= 1):
		Log("\n\n	----	Length Checking")

	length = size;

	if (flag >= 1):
		Log("\n\n	Length is : " + length)

	if (length == 1):
		if (flag >= 1):
			Log("	Thats... Thats a letter!	Password is non-existent... ERROR!!!")
			if (flag > 1):
				Log("	No points awarded")
			elif (length < 5):
				if (flag >= 1):
					Log("	Password is very weak!")
				if (flag > 1):
					Log("	No points awarded")

	elif (length < 10):
		if (flag >= 1):
			Log("	Password is weak!")
			if (flag > 1):
				Log("	Integrity + 1")
			
		total[1] += 1

	elif (length < 15):
		if (flag >= 1):
			Log("	Password is average")
			if (flag > 1):
				Log("	Integrity + 2")
			
		total[1] += 2

	elif (length < 20):
		if (flag >= 1):
			Log("	Password is good!")
			if (flag > 1):
				Log("	Integrity + 3")
			
		total[1] += 3

	elif (length > 19):
		if (flag >= 1):
			Log("	Password is strong!")
			if (flag > 1):
				Log("	Integrity + 4")
			
		total[1] += 4
	
	return total;

def pairscounter(passwd, size, flag, totalcarry):

	total[3]
	total[0] = totalcarry[0]
	total[1] = totalcarry[1]
	total[2] = totalcarry[2]

	if (flag >= 1):
		Log("\n\n	----	Pair Counting \n")

	length = size;
	firstchar;
	repeatedcounter = 0;
	paircounter = 0;

	#Pairing Analysis___________________________________________________

	firstchar = passwd[0];

	for m in range(length + 1):
		firstchar = passwd[m - 1]
		if (firstchar == passwd[m]):
			if (flag > 1):
				Log("	Repeated character at " << m - 1 << "," << m << "	")
				Log(passwd[m] << "," << passwd[m - 1] << "	")
			repeatedcounter = repeatedcounter + 1
		
	if (flag >= 1):
		Log("\n	There are " << repeatedcounter << " repeated pairs")

	for u in range(length-1):															# For each letter in the password
		for v in range(53):																# and for each pair
			if (passwd[u] == commonpairs[0][v] and passwd[u + 1] == commonpairs[1][v]):				# look for a matching pair
				paircounter = paircounter + 1												# if found add to counter

				if (flag > 1):
					LogIn("	Common Pair Detected at " << u << "," << u + 1 << "	")
					LogIn(passwd[u] << "," << passwd[u + 1] << "	")
					LogIn("Pair " << v << ": " << commonpairs[0][v] << commonpairs[1][v] << "\n")

	if (flag >= 1):
		Log("\n	There are " << paircounter << " common pairs")

	# Feedback and Score

	if ((paircounter > length / 2) or (repeatedcounter > length / 2)):
		if (flag >= 1):
			LogIn("	Your password is predictable")
			LogIn(" as more than half of the password is made of ")
	
	if (paircounter > length / 2):
		if (flag >= 1):
			LogIn("common pairs")
		
	if ((paircounter > length / 2) and (repeatedcounter > length / 2)):
		if (flag >= 1):
			LogIn(" and ")
		
	if (repeatedcounter > length / 2):
		if (flag >= 1):
			LogIn("repeated pairs")
		
	elif ((paircounter > length / 4) or (repeatedcounter > length / 4)):
		if (flag >= 1):
			LogIn("	Your password may be predictable")
			LogIn(" as more than a quarter of the password is made of ")
		
		if (paircounter > length / 4):
			if (flag >= 1):
				LogIn("common pairs")
			
			total[1] += 2
		
		if ((paircounter > length / 4) and (repeatedcounter > length / 4)):
			if (flag >= 1):
				LogIn(" and ")
			
		if (repeatedcounter > length / 4):
			if (flag >= 1):
				LogIn("repeated pairs")
			
			total[0] += 2
		
	elif ((paircounter < length / 4) or (repeatedcounter < length / 4)):
		if (flag >= 1):
			Log("	Your password is likely unpredictable as less than a")
			LogIn("	quarter of the password is made of ")
		
		if (paircounter < length / 4):
			if (flag >= 1):
				LogIn("common pairs")
			
			total[1] += 2;
		
		if ((paircounter < length / 4) and (repeatedcounter < length / 4)):
			if (flag >= 1):
				LogIn(" and ");
			
		if (repeatedcounter < length / 4):
			if (flag >= 1):
				LogIn("repeated pairs")
			
			total[0] += 2
		
	if (flag >= 1):
		LogIn("\n");
	
	return total;


def wordscounter(passwd, size, flag, totalcarry):

	total[3];
	total[0] = totalcarry[0]
	total[1] = totalcarry[1]
	total[2] = totalcarry[2]

	if (flag >= 1):
		Log("\n\n	----	Word Counting \n");

	length = size;
	newwordflag = 0;
	wordcounter = 0;
	word;

	#Word Detector__________________________________

	words = [];												# Declare a vector of strings

	w = 0;
	while (w < length + 1):																# As program parses the password, while the character in focus is not the last (redundant?)
		if (passwd[w] == char(32) or passwd[w] == char(95) or w == length):				# Checking if the next character is a (valid) space (this should be improved to cover other subs)
			for newwordflag in range(newwordflag < w):									# Begin creating a container
				word.push_back(passwd[x]);												# Push back each character in the detected word

			words.push_back(word);					# Save the detected word
			word.clear();							# And clear this container for future use

			wordcounter += 1;						# Add a word to the wordscounter
			newwordflag = w + 1;					# Move the start of the next word to the next valid word
			
			w+=1									# We've checked this letter, move along the string

	# Grading and Feedback

	if (wordcounter > 0):
		if (flag >= 1):
			Log("\n	The supplied password has " << wordcounter << " words in it : \n")

		for y in range ( y < wordcounter):
			if (flag >= 1):
				LogIn("	Word:	" << y + 1)
				LogIn(" : " << words[y] << "\n")
			
		if (wordcounter >= 4):
			total[2] += 4;
			if (flag > 1):
				Log("	Memorability + 4");
			
		elif (wordcounter == 3):
			total[2] += 3;
			if (flag > 1):
				Log("	Memorability + 3");
			
		elif (wordcounter == 2):
			total[2] += 2;
			if (flag > 1):
				Log("	Memorability + 2");

		elif (wordcounter == 1 and length > 14):
			total[2] += 3;
			if (flag > 1) :
				Log("	Memorability + 3");
			
		elif (wordcounter == 1 and length > 9):
			total[2] += 2;
			if (flag > 1):
				Log("	Memorability + 2");
			
		elif (wordcounter == 1):
			total[2] += 1;
			if (flag > 1):
				Log("	Memorability + 1");
			
	return total;

def subscounter(passwd, size, flag, totalcarry):

	total[3];
	total[0] = totalcarry[0]
	total[1] = totalcarry[1]
	total[2] = totalcarry[2]

	goodsubs = 0
	likelysubs = 0
	badsubs = 0
	subcounter = 0

	if (flag >= 1):
		Log("\n\n	----	Substitution Counting \n");

	length = size
	matchleft = 0
	matchright = 0

	for f in range(length + 1):					# Run through Password
		for g in range(g < 22):						# Run through substitutions

			#Log("		Checking subs " << g + 1 << "	: " << subs[0][g] << "," << subs[1][g] << " On letter " << f );			# When uncommented this will produce length x 22 lines

			if (passwd[f] == subs[0][g]):			# Detect a subs character

				if (flag > 1):
					Log("	Substituted Character detected at position " << f << ", character : '" << passwd[f] << "'");

				for h in range (h < 53):			# Run through list of common pairings to find correct pairing
															# Then check against character left for what a common pairing would like w'out subs
					if ((subs[1][g] == commonpairs[1][h] and passwd[f - 1] == commonpairs[0][h]) and f - 1 > -1):	# look for a matching pair on the left without leaking
						matchleft = 1
					
					# Then check against character right for what a common pairing would like w'out subs
					if (subs[1][g] == commonpairs[0][h] and passwd[f + 1] == commonpairs[1][h]):
						matchright = 1
					

				# Readout

				if (matchleft == 1 or matchright == 1):
					if (matchleft == 1 and matchright == 1):
						if (flag > 1):
							LogIn("	Likely Substituted Character detected at " << f - 1 << "," << f << "," << f + 1)
							Log(" '" << passwd[f - 1] << "', '" << passwd[f] << "', '" << passwd[f + 1] << "'")
						
						badsubs += 1
						subcounter += 1
					
					elif (matchleft == 1):
						if (flag > 1):
							Log("	Possible Substituted Character detected at " << f - 1 << "," << f << "	")
						
						likelysubs += 1;
						subcounter += 1;
					
					elif (matchright == 1):
						if (flag > 1):
							Log("	Possible Substituted Character detected at " << f << "," << f + 1 << "	");
						
						likelysubs += 1;
						subcounter += 1;
					
				
				elif (matchleft == 0 and matchright == 0):
					if (flag > 1):
						Log("	Character detected at " << f << ", '" << passwd[f] << "'	Adds to Entropy");
					
					goodsubs += 1;
					subcounter += 1;
				
				matchleft = 0;
				matchright = 0;

	Log("\n");

	#Counter
	if (subcounter > 0):
		if (goodsubs > 0):
			total[0] += 4;
			if (flag > 0):
				Log("	Very Good substitutions!");
				if (flag > 1):
					Log("\n	Entropy + 4");
				
		if (likelysubs > 0):
			total[0] += 3;
			if (flag > 0):
				Log("	Good substitutions!");
				if (flag > 1):
					Log("\n	Entropy + 3");
				
		if (badsubs > 0):
			total[0] += 2;
			if (flag > 0):
				Log("	Substitutions!");
				if (flag > 1):
					Log("\n	Entropy + 2");
				
	elif (goodsubs == 0 or likelysubs == 0 or badsubs == 0):
		if (flag >= 1):
			Log("	No substituted characters detected");
		
	return total;

def main():

	flag = 0;			# 0 for minimal, 1 for basic, 2 for in-depth
	password[32];
	length = 0;

	total;
	initial = [ 0,0,0 ];

	print("running main")

	passwordstr = "password";				# Use the function to get the password

	strcpy_s(password, passwordstr.c_str());		# String into char array
	length = passwordstr.len();					# Extract password length from string

	total = charcounter(password, length, flag, initial);
	total = lengthcounter(length, flag, total);
	total = pairscounter(password, length, flag, total);
	total = wordscounter(password, length, flag, total);
	total = subscounter(password, length, flag, total);

	Log("\n	Entropy : " << total[0] << " / 12,	Integrity : " << total[1] << " / 6,	Memorability : " << total[2] << " / 4");


	return total
	# ?

# LOG
#/
#/ Add repeated pair checking - Yes
# Natural Language detection - more or less
# Common word detection - sorta
#
# Length to time Brute force calc - No
# Account for entropy - Yes
# Maybe replace the character counters with selection that creates / modifies and pushes back a pair - Not Needed
#
# Split into functions - Yes
# Create a "debug" flag for console readout that can be supplied to the functions - Yes
# Create an array that functions will return once complete that can be used for feedback - Yes
#
# eg, string total = strenG4
# "Strength", so debug code displays "strength" when in code it looks like Log(x, " checker...")
# "G" password is good
# "4" Grade is 4
# maybe add in an entropy grade?

# grade idea ->
# int grade [3] = {0,0,0}
# where array represents {E, I, M}
#
# Entropy - lack of order or predictability; gradual decline into disorder		- Good Substitutions (more is better)/ Mix of characters (where more is better)	-> Defeats People and Predictive Machines
# Integrity - the state of being whole and undivided							- Length (more is better)/ Common Pairings (less is better)						-> Defeats Brute Forcing Mechanisms
# Memorability - The quality or fact of being memorable.						- Number of words (more is better)/ Common Substitutions (less is better)		-> Defeats "Shoulder Peeping" (people)
