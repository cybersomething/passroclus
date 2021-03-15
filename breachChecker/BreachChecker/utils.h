// Code for loading files sourced from Adam Sampson's string searching lab exercise in CMP201.

#ifndef UTILS_H
#define UTILS_H

#include <string>

/** Integer type that can hold a position within an array. */
using Position = long int;

/** Print an error message and abort the program. */
void die(const std::string& msg);

/** Load the whole of a text file into str. */
void load_file(const std::string& filename, std::string& str);

/** Check first letter of password and load the the text from the appropriate common password file into str. */
void load_list(std::string& str, char x);

#endif
