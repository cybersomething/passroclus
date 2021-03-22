#include <iostream>                            // c++ standard libraries in
#include <cstdio>
#include <cassert>
#include <vector>			// Co-Star Data structure of the show
#include <string>			// Star data structure of the show
#include <chrono>			// The clock standard library
#include <cstring>			// Expanded String Library

// Password strength analyser by P.CAPTAIN
// (Proof of concept)
// Checks a password useability by assessing 3 key areas of the password
// Entropy		- Where more complexity is desired
// Integrity	- Where concepts used in password creation to defeat machines guessing &/or bruteforcing a password are desired
// Memorability	- If a human being could remember the password... This is good if you need to know the passowrd, bad if someone sees it.

#define Log(x)  cout << x << endl
#define LogIn(x) cout << x

using std::chrono::duration_cast;
using std::chrono::nanoseconds;							 // Setting up the clock to measure time in an appropriate format.
typedef std::chrono::steady_clock the_clock;             // Synchronises the clock

using namespace std;

#pragma region Populated Arrays
char alphabet[26] = { char(97), char(98), char(99), char(100), char(101), char(102), char(103), char(104),
						char(105), char(106), char(107), char(108), char(109), char(110), char(111), char(112), char(113),
						char(114), char(115), char(116), char(117), char(118), char(119), char(120), char(121), char(122) };
char ALPHABET[26] = { char(65), char(66), char(67), char(68), char(69), char(70), char(71), char(72),
						char(73), char(74), char(75), char(76), char(77), char(78), char(79), char(80), char(81),
						char(82), char(83), char(84), char(85), char(86), char(87), char(88), char(89), char(90) };
char numbers[10] = { char(48), char(49), char(50), char(51), char(52), char(53), char(54), char(55), char(56), char(57) };
char symbols[10] = { char(32), char(33), char(34), char(35), char(36), char(37), char(38), char(39), char(63), char(64) };

char commonpairs[2][53]{
	{'t', 'h', 'a', 'i', 'e', 'n', 'r', 'e', 'e', 'o', 't', 'h', 'e', 'e', 's', 'n', 'o', 'a', 'h', 'a', 'i', 'n', 'i', 'o', 'e', 'o',
		't', 'a', 't', 's', 'm', 's', 'n', 'w', 'v', 'l', 'n', 't', 'a', 'd', 'o', 's', 'd', 'l', 't', 'e', 'r', 'a', 'd', 'e', 'r', 'r', 's'},
	{'h', 'e', 'n', 'n', 'r', 'd', 'e', 'd', 's', 'u', 'o', 'a', 'n', 'a', 't', 't', 'n', 't', 'i', 's', 't', 'g', 's', 'r', 't', 'f',
		'i', 'r', 'e', 'e', 'e', 'a', 'e', 'a', 'e', 'e', 'o', 'a', 'l', 'e', 't', 'o', 't', 'l', 't', 'l', 'o', 'd', 'i', 'w', 'a', 'i', 'h'}
};

char subs[2][22]{
	{'@', '8', '(', '6', '3', '#', '9', '#', '1', '!', '<', '1', 'i', '0', '9', '5', '$', '+', '>', '<', '%', '?'},
	{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'k', 'l', 'l', 'o', 'q', 's', 's', 't', 'v', 'v', 'x', 'y'}
};
//for (int a = 0; a < 26; a++) {
//	alphacounter[a] = 0;
//	ALPHAcounter[a] = 0;
//}
//
//for (int b = 0; b < 10; b++) {
//	numbercounter[b] = 0;
//	symbolcounter[b] = 0;
//}
#pragma endregion Arrays contains all the populated arrays used in analaysis

string getpassword() {

	int validflag = 0;
	string passwordstr = "default";

	Log("\n\n\n	Welcome to the password checking Program");
	Log("	ENTER YOUR PASSWORD BELOW FOR ANALYSIS");

	while (validflag == 0) {

		LogIn("\n---->	");
		//std::getline(std::cin, passwordstr);
		std::getline(std::cin, passwordstr);
		Log("\n	Looking at: '" << passwordstr << "'");

		int length = 0;
		length = passwordstr.length();


		if (length == 0) {
			Log("	Invalid, Please enter a password\n");
		}
		else if (length > 32) {
			Log("	Password is too long! What type of password is that anyway?\n");
		}
		else if (length <= 32) {
			validflag = 1;
		}
	}

	return passwordstr;
}

int* charcounter(char passwd[], int size, int flag, int totalcarry[]) {

	int length = size;

	int totalalpha = 0;
	int totalALPHA = 0;
	int totalnumber = 0;
	int totalsymbol = 0;

	static int total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	int alphacounter[26] = { 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	int ALPHAcounter[26] = { 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	int numbercounter[10] = { 0,0,0,0,0,0,0,0,0,0 };
	int symbolcounter[10] = { 0,0,0,0,0,0,0,0,0,0 };

	if (flag == 1) {
		Log("\n\n	----	Character Counting \n");
	}

	//Character Counter_________________________________________________

	for (int i = 0; i < 26; i++) {					// Run through all Alphabet lists
		for (int j = 0; j < length; j++) {			// For each letter in the password
			if (passwd[j] == alphabet[i]) {
				if (flag > 1) {
					Log("	lowercase DETECTED " << alphabet[i]);
				}
				alphacounter[i] += 1;// Counter for lowercase
				totalalpha += 1;
			}
			if (passwd[j] == ALPHABET[i]) {
				if (flag > 1) {
					Log("	CAPITAL DETECTED " << ALPHABET[i]);
				}
				ALPHAcounter[i] += 1;// Counter for CAPITAL
				totalALPHA += 1;
			}
		}
	}

	for (int k = 0; k < 10; k++) {					// Run through all Number/ Symbol lists
		for (int l = 0; l < length; l++) {			// For each letter in the password
			if (passwd[l] == numbers[k]) {
				if (flag > 1) {
					Log("	number DETECTED " << numbers[k]);
				}
				numbercounter[k] += 1;// Counter for numbers 
				totalnumber += 1;
			}
			if (passwd[l] == symbols[k]) {
				if (flag > 1) {
					Log("	symbol DETECTED " << symbols[k]);
				}
				symbolcounter[k] += 1;// Counter for symbols
				totalsymbol += 1;
			}
		}
	}

	// Breakdown readout

	if (flag > 1) {
		Log("\n	The password consists of \n");
	}

	for (int m = 0; m < 26; m++) {					// Run through all Alphabet lists
		if (alphacounter[m] >= 1) {
			if (flag > 1) {
				Log("	Character:	'" << alphabet[m] << "'		Amount: " << alphacounter[m]);
			}
		}
		if (ALPHAcounter[m] >= 1) {
			if (flag > 1) {
				Log("	Character:	'" << ALPHABET[m] << "'		Amount: " << ALPHAcounter[m]);
			}
		}
	}

	for (int n = 0; n < 10; n++) {					// Run through all symbol lists
		if (numbercounter[n] >= 1) {
			if (flag > 1) {
				Log("	Character:	'" << numbers[n] << "'		Amount: " << numbercounter[n]);
			}
		}
		if (ALPHAcounter[n] >= 1) {
			if (flag > 1) {
				Log("	Character:	'" << symbols[n] << "'		Amount: " << symbolcounter[n]);
			}
		}
	}

	if (flag >= 1) {
		Log("\n	The password consists of in total: \n");

		Log("	Lowercase characters:	" << totalalpha);
		Log("	UPPERCASE characters:	" << totalALPHA);
		Log("	Numbers             :	" << totalnumber);
		Log("	Symbols             :	" << totalsymbol);
	}

	// Suggestions and Grade

	if (totalALPHA < 2) {
		if (flag >= 1) {
			Log("	Your password contains a low amount of uppercase characters!");
		}
	}
	else {
		if (flag > 1) {
			LogIn("	Good Amount of uppercase, Entropy + 1");
		}
		total[0] += 1;
	}
	if (totalnumber < 2) {
		if (flag >= 1) {
			Log("	Your password contains a low amount of numbers!");
		}
	}
	else {
		if (flag > 1) {
			LogIn("	Good Amount of numbers, Entropy + 1 \n");
		}
		total[0] += 1;
	}
	if (totalsymbol < 2) {
		if (flag >= 1) {
			Log("	Your password contains a low amount of symbols! \n");
		}
	}
	else {
		if (flag > 1) {
			LogIn("	Good Amount of symbols, Entropy + 1 \n");
		}
		total[0] += 1;
	}
	if (totalalpha > 10) {
		if (flag >= 1) {
			Log("	Your password contains a lot of lowercase! \n");
		}
	}
	else {
		if (flag > 1) {
			LogIn("	Good Amount of lowercase, Entropy + 1 \n");
		}
		total[0] += 1;
	}
	return total;
}

int* lengthcounter(int size, int flag, int totalcarry[]) {

	static int total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	if (flag >= 1) {
		Log("\n\n	----	Length Checking");
	}

	int length = size;

	if (flag >= 1) {
		Log("\n\n	Length is : " << length);
	}

	if (length == 1) {
		if (flag >= 1) {
			Log("	Thats... Thats a letter!	Password is non-existent... ERROR!!!");
			if (flag > 1) {
				Log("	No points awarded");
			}
		}
	}
	else if (length < 5) {
		if (flag >= 1) {
			Log("	Password is very weak!");
			if (flag > 1) {
				Log("	No points awarded");
			}
		}
	}
	else if (length < 10) {
		if (flag >= 1) {
			Log("	Password is weak!");
			if (flag > 1) {
				Log("	Integrity + 1");
			}
		}
		total[1] += 1;
	}
	else if (length < 15) {
		if (flag >= 1) {
			Log("	Password is average");
			if (flag > 1) {
				Log("	Integrity + 2");
			}
		}
		total[1] += 2;
	}
	else if (length < 20) {
		if (flag >= 1) {
			Log("	Password is good!");
			if (flag > 1) {
				Log("	Integrity + 3");
			}
		}
		total[1] += 3;
	}
	else if (length > 19) {
		if (flag >= 1) {
			Log("	Password is strong!");
			if (flag > 1) {
				Log("	Integrity + 4");
			}
		}
		total[1] += 4;
	}
	return total;
}

int* pairscounter(char passwd[], int size, int flag, int totalcarry[]) {

	static int total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	if (flag >= 1) {
		Log("\n\n	----	Pair Counting \n");
	}

	int length = size;
	char firstchar;
	int repeatedcounter = 0;
	int paircounter = 0;

	//Pairing Analysis___________________________________________________

	firstchar = passwd[0];

	for (int m = 1; m < length + 1; m++) {
		firstchar = passwd[m - 1];
		if (firstchar == passwd[m]) {
			if (flag > 1) {
				LogIn("	Repeated character at " << m - 1 << "," << m << "	");
				Log(passwd[m] << "," << passwd[m - 1] << "	");
			}
			repeatedcounter = repeatedcounter + 1;
		}
	}

	if (flag >= 1) {
		Log("\n	There are " << repeatedcounter << " repeated pairs");
	}

	for (int u = 0; u < length - 1; u++) {															// For each letter in the password
		for (int v = 0; v < 53; v++) {																// and for each pair
			if (passwd[u] == commonpairs[0][v] && passwd[u + 1] == commonpairs[1][v]) {				// look for a matching pair
				paircounter = paircounter + 1;														// if found add to counter

				if (flag > 1) {
					LogIn("	Common Pair Detected at " << u << "," << u + 1 << "	");
					LogIn(passwd[u] << "," << passwd[u + 1] << "	");
					LogIn("Pair " << v << ": " << commonpairs[0][v] << commonpairs[1][v] << "\n");
				}
			}
		}
	}

	if (flag >= 1) {
		Log("\n	There are " << paircounter << " common pairs");
	}

	// Feedback and Score

	if ((paircounter > length / 2) || (repeatedcounter > length / 2)) {
		if (flag >= 1) {
			LogIn("	Your password is predictable");
			LogIn(" as more than half of the password is made of ");
		}
	}
	if (paircounter > length / 2) {
		if (flag >= 1) {
			LogIn("common pairs");
		}
	}
	if ((paircounter > length / 2) && (repeatedcounter > length / 2)) {
		if (flag >= 1) {
			LogIn(" and ");
		}
	}
	if (repeatedcounter > length / 2) {
		if (flag >= 1) {
			LogIn("repeated pairs");
		}
	}
	else if ((paircounter > length / 4) || (repeatedcounter > length / 4)) {
		if (flag >= 1) {
			LogIn("	Your password may be predictable");
			LogIn(" as more than a quarter of the password is made of ");
		}
		if (paircounter > length / 4) {
			if (flag >= 1) {
				LogIn("common pairs");
			}
			total[1] += 2;
		}
		if ((paircounter > length / 4) && (repeatedcounter > length / 4)) {
			if (flag >= 1) {
				LogIn(" and ");
			}
		}
		if (repeatedcounter > length / 4) {
			if (flag >= 1) {
				LogIn("repeated pairs");
			}
			total[0] += 2;
		}
	}
	else if ((paircounter < length / 4) || (repeatedcounter < length / 4)) {
		if (flag >= 1) {
			Log("	Your password is likely unpredictable as less than a");
			LogIn("	quarter of the password is made of ");
		}
		if (paircounter < length / 4) {
			if (flag >= 1) {
				LogIn("common pairs");
			}
			total[1] += 2;
		}
		if ((paircounter < length / 4) && (repeatedcounter < length / 4)) {
			if (flag >= 1) {
				LogIn(" and ");
			}
		}
		if (repeatedcounter < length / 4) {
			if (flag >= 1) {
				LogIn("repeated pairs");
			}
			total[0] += 2;
		}
	}
	if (flag >= 1) {
		LogIn("\n");
	}
	return total;
}

int* wordscounter(char passwd[], int size, int flag, int totalcarry[]) {

	static int total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	if (flag >= 1) {
		Log("\n\n	----	Word Counting \n");
	}

	int length = size;
	int newwordflag = 0;
	int wordcounter = 0;
	string word;

	//Word Detector__________________________________

	vector<string> words;												// Declare a vector of strings

	int w = 0;
	while (w < length + 1) {																// As program parses the password, while the character in focus is not the last (redundant?)
		if (passwd[w] == char(32) || passwd[w] == char(95) || w == length) {				// Checking if the next character is a (valid) space (this should be improved to cover other subs)
			for (int x = newwordflag; x < w; x++) {											// Begin creating a container
				word.push_back(passwd[x]);													// Push back each character in the detected word
			}

			words.push_back(word);					// Save the detected word
			word.clear();							// And clear this container for future use

			wordcounter += 1;						// Add a word to the wordscounter
			newwordflag = w + 1;					// Move the start of the next word to the next valid word
		}
		w++;										// We've checked this letter, move along the string
	}

	// Grading and Feedback

	if (wordcounter > 0) {
		if (flag >= 1) {
			Log("\n	The supplied password has " << wordcounter << " words in it : \n");
		}

		for (int y = 0; y < wordcounter; y++) {
			if (flag >= 1) {
				LogIn("	Word:	" << y + 1);
				LogIn(" : " << words[y] << "\n");
			}
		}

		if (wordcounter >= 4) {
			total[2] += 4;
			if (flag > 1) {
				Log("	Memorability + 4");
			}
		}
		else if (wordcounter == 3) {
			total[2] += 3;
			if (flag > 1) {
				Log("	Memorability + 3");
			}
		}
		else if (wordcounter == 2) {
			total[2] += 2;
			if (flag > 1) {
				Log("	Memorability + 2");
			}
		}
		else if (wordcounter == 1 && length > 14) {
			total[2] += 3;
			if (flag > 1) {
				Log("	Memorability + 3");
			}
		}
		else if (wordcounter == 1 && length > 9) {
			total[2] += 2;
			if (flag > 1) {
				Log("	Memorability + 2");
			}
		}
		else if (wordcounter == 1) {
			total[2] += 1;
			if (flag > 1) {
				Log("	Memorability + 1");
			}
		}
	}
	return total;
}

int* subscounter(char passwd[], int size, int flag, int totalcarry[]) {

	static int total[3];
	total[0] = totalcarry[0];
	total[1] = totalcarry[1];
	total[2] = totalcarry[2];

	int goodsubs = 0;
	int likelysubs = 0;
	int badsubs = 0;
	int subcounter = 0;

	if (flag >= 1) {
		Log("\n\n	----	Substitution Counting \n");
	}

	int length = size;
	bool matchleft = 0;
	bool matchright = 0;

	for (int f = 1; f < length + 1; f++) {					// Run through Password
		for (int g = 0; g < 22; g++) {						// Run through substitutions

			//Log("		Checking subs " << g + 1 << "	: " << subs[0][g] << "," << subs[1][g] << " On letter " << f );			// When uncommented this will produce length x 22 lines

			if (passwd[f] == subs[0][g]) {				// Detect a subs character

				if (flag > 1) {
					Log("	Substituted Character detected at position " << f << ", character : '" << passwd[f] << "'");
				}

				for (int h = 0; h < 53; h++) {				// Run through list of common pairings to find correct pairing
						// Then check against character left for what a common pairing would like w'out subs
					if ((subs[1][g] == commonpairs[1][h] && passwd[f - 1] == commonpairs[0][h]) && f - 1 > -1) {		// look for a matching pair on the left without leaking
						matchleft = 1;
					}
					// Then check against character right for what a common pairing would like w'out subs
					if (subs[1][g] == commonpairs[0][h] && passwd[f + 1] == commonpairs[1][h]) {
						matchright = 1;
					}
				}

				// Readout

				if (matchleft == 1 || matchright == 1) {
					if (matchleft == 1 && matchright == 1) {
						if (flag > 1) {
							LogIn("	Likely Substituted Character detected at " << f - 1 << "," << f << "," << f + 1);
							Log(" '" << passwd[f - 1] << "', '" << passwd[f] << "', '" << passwd[f + 1] << "'");
						}
						badsubs += 1;
						subcounter += 1;
					}
					else if (matchleft == 1) {
						if (flag > 1) {
							Log("	Possible Substituted Character detected at " << f - 1 << "," << f << "	");
						}
						likelysubs += 1;
						subcounter += 1;
					}
					else if (matchright == 1) {
						if (flag > 1) {
							Log("	Possible Substituted Character detected at " << f << "," << f + 1 << "	");
						}
						likelysubs += 1;
						subcounter += 1;
					}
				}
				else if (matchleft == 0 && matchright == 0) {
					if (flag > 1) {
						Log("	Character detected at " << f << ", '" << passwd[f] << "'	Adds to Entropy");
					}
					goodsubs += 1;
					subcounter += 1;
				}
				matchleft = 0;
				matchright = 0;
			}
		}
	}

	Log("\n");

	//Counter
	if (subcounter > 0) {
		if (goodsubs > 0) {
			total[0] += 4;
			if (flag > 0) {
				Log("	Very Good substitutions!");
				if (flag > 1) {
					Log("\n	Entropy + 4");
				}
			}
		}
		if (likelysubs > 0) {
			total[0] += 3;
			if (flag > 0) {
				Log("	Good substitutions!");
				if (flag > 1) {
					Log("\n	Entropy + 3");
				}
			}
		}
		if (badsubs > 0) {
			total[0] += 2;
			if (flag > 0) {
				Log("	Substitutions!");
				if (flag > 1) {
					Log("\n	Entropy + 2");
				}
			}
		}
	}
	else if (goodsubs == 0 || likelysubs == 0 || badsubs == 0) {
		if (flag >= 1) {
			Log("	No substituted characters detected");
		}
	}
	return total;
}

int main() {

	int flag = 0;			// 0 for minimal, 1 for basic, 2 for in-depth
	char password[32];
	int length = 0;

	int* total;
	int initial[3] = { 0,0,0 };

	// Debug
	/*Log("	Indicate your debug preference, 0 none, 1 some, 2 full.");
	std::cin >> flag;*/

	// ? 
	// password = recievefromAPI()

	string passwordstr = getpassword();				// Use the function to get the password

	strcpy_s(password, passwordstr.c_str());		// String into char array
	length = passwordstr.length();					// Extract password length from string

	the_clock::time_point start = the_clock::now();	// Start timing

	total = charcounter(password, length, flag, initial);
	total = lengthcounter(length, flag, total);
	total = pairscounter(password, length, flag, total);
	total = wordscounter(password, length, flag, total);
	total = subscounter(password, length, flag, total);

	if (flag > 0) {
		Log("\n	---------------------------> " + passwordstr + " <---------------------------\n");
	}

	Log("\n	Entropy : " << total[0] << " / 12,	Integrity : " << total[1] << " / 6,	Memorability : " << total[2] << " / 4");

	the_clock::time_point end = the_clock::now();		// Stop timing

	auto time_taken = duration_cast<nanoseconds>(end - start).count();		// Work out time taken and display the result
	Log("\n\n	Program took " << time_taken << " nanoseconds\n");


	// return total[]; 
	// ?
}

// LOG
//
// Add repeated pair checking - Yes
// Natural Language detection - more or less
// Common word detection - sorta
//
// Length to time Brute force calc - No
// Account for entropy - Yes
// Maybe replace the character counters with selection that creates / modifies and pushes back a pair - Not Needed
//
// Split into functions - Yes
// Create a "debug" flag for console readout that can be supplied to the functions - Yes
// Create an array that functions will return once complete that can be used for feedback - Yes
//
// eg, string total = strenG4
// "Strength", so debug code displays "strength" when in code it looks like Log(x, " checker...")
// "G" password is good
// "4" Grade is 4
// maybe add in an entropy grade?

// grade idea ->
// int grade [3] = {0,0,0}
// where array represents {E, I, M}
//
// Entropy - lack of order or predictability; gradual decline into disorder		- Good Substitutions (more is better)/ Mix of characters (where more is better)	-> Defeats People and Predictive Machines
// Integrity - the state of being whole and undivided							- Length (more is better)/ Common Pairings (less is better)						-> Defeats Brute Forcing Mechanisms
// Memorability - The quality or fact of being memorable.						- Number of words (more is better)/ Common Substitutions (less is better)		-> Defeats "Shoulder Peeping" (people)
