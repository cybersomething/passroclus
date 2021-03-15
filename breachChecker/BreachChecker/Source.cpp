/* This program was originally sourced from https://www.geeksforgeeks.org/boyer-moore-algorithm-good-suffix-heuristic/ [28/11/19]
Some adaptions have been made */

// Code for loading files sourced from Adam Sampson's string searching lab exercise in CMP201.

#include <chrono>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <list>
#include <string>

#include "utils.h"

#define measure_num 1

using std::chrono::duration_cast;
using std::chrono::milliseconds;
using std::cout;
using std::endl;
using std::list;
using std::string;
using std::ofstream;

typedef std::chrono::steady_clock the_clock;

bool breach = false; // Breach variable for return value

// Preprocessing for strong good suffix rule 
void ss_preprocess(int* shift, int* border_pos,
	char* pat)
{
	Position pat_len = strlen(pat);
	Position i = pat_len;
	Position j = pat_len + 1;
	border_pos[i] = j;

	while (i > 0)
	{
		// If characters at i-1 and j-1 do not match, continue searching to right of the pattern for border
		while (j <= pat_len && pat[i - 1] != pat[j - 1])
		{
			/* The character before the occurrence of t in
			   pattern is different than the mismatching character in pattern,
			   stop skipping the occurrences and shift the pattern
			   from i to j */
			if (shift[j] == 0)
				shift[j] = j - i;

			// Update the position of next border  
			j = border_pos[j];
		}
		// p[i-1] matches p[j-1], border is found. Store the beginning position of border
		i--; j--;
		border_pos[i] = j;
	}
}


// Preprocessing for case 2 
void case2_preprocess(int* shift, int* border_pos,
	char* pat)
{
	Position pat_len = strlen(pat);
	int i, j;
	j = border_pos[0];
	for (i = 0; i <= pat_len; i++)
	{
		// If shift[i] is 0, store border position as first character of pattern
		if (shift[i] == 0)
			shift[i] = j;

		// Suffix becomes shorter than border position[0], use position of next widest border
		if (i == j)
			j = border_pos[j];
	}
}

void boyerMoore(const string& text, char* pat)
{
	Position pat_len = strlen(pat);
	Position text_len = text.size();

	// s is shift of the pattern with respect to text 
	int s = 0, j, k;

	int* border_pos = new int[pat_len + 1];
	int* shift = new int[pat_len + 1];

	// Set all shift values to 0 initially
	for (int i = 0; i < pat_len + 1; i++) shift[i] = 0;

	// Do preprocessing 
	ss_preprocess(shift, border_pos, pat);
	case2_preprocess(shift, border_pos, pat);

	while (s <= text_len - pat_len)
	{

		j = pat_len - 1;

		// While pattern and text characters match and match not found, keep checking
		while ((j >= 0 && pat[j] == text[s + j]) && !breach)

			j--;

			// If there is a match, j will have reached -1 in the above loop
			if (j < 0)
			{
				// Previous character is not a new line or return (ie. empty) and this is not the beginning of the text file, this is a partial match (eg. 'abc' in 'abcd')
				if ((s != 0) && (text[s + j] != '\n') && (text[s + j] != '\r'))
				{
					// Only a partial match, continue searching
					s += shift[j + 1];
				}
				// Previous character is a new line or return, or this is the beginning of the text file
				else
				{
					int m = ((s + j) + 1); // Beginning of match

						// Check that character immediately after pattern is a new line, return or equal to the end of the file
						if ((text[m + pat_len] == '\n') || (text[m + pat_len] == '\r') || ((s + pat_len) == text_len))
						{
							breach = true; // Match found, set breach variable to true
							s = text_len;
						}
						else
						{
							// Only a partial match, continue searching
							s += shift[j + 1];
						}
				}
			}
			else
				// Mismatch occurred, continue shifting
				s += shift[j + 1];
		}

	// Remove pointers
	delete[] border_pos;
	delete[] shift;
}

int main()
{
	string text;

	// Password to search for
	char pat[] = "syzygy";

	// Check first letter of password and load approriate wordlist
	load_list(text, pat[0]);

	// Boyer-Moore algorithm runs here
	boyerMoore(text, pat);

	// Print result
	if (breach)
	{
		cout << "The password '" << pat << "' was found to have been breached." << endl << endl;
	}
	else
	{
		cout << "The password '" << pat << "' was not found to have been breached." << endl << endl;
	}

	return 0;
}