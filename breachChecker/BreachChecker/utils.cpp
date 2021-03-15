// Code for loading files sourced from Adam Sampson's string searching lab exercise.

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "utils.h"

using std::cerr;
using std::cout;
using std::ifstream;
using std::string;
using std::vector;

void die(const string& msg) {
	cerr << "Error: " << msg << "\n";
#ifdef _DEBUG
	abort();
#else
	exit(1);
#endif
}

void load_file(const string& filename, string& str) {
	std::string directory = "";
	for (int i = 0; i < 6; i++) {
		ifstream f(directory + filename, std::ios_base::binary);
		if (!f.good()) {
			directory = "../" + directory;
			continue;
		}

		// Seek to the end of the file to find its length.
		f.seekg(0, std::ios_base::end);
		const size_t length = f.tellg();

		// Seek back to the start of the file and read the data.
		vector<char> buf(length);
		f.seekg(0);
		f.read(buf.data(), length);
		str.assign(buf.begin(), buf.end());

		return;
	}

	die("Unable to find " + filename);
}

void load_list(std::string& str, char x) {
	if (x == 'a')
	{
		load_file("a.txt", str);
	}
	else if (x == 'b')
	{
		load_file("b.txt", str);
	}
	else if (x == 'c')
	{
		load_file("c.txt", str);
	}
	else if (x == 'd')
	{
		load_file("d.txt", str);
	}
	else if (x == 'e')
	{
		load_file("e.txt", str);
	}
	else if (x == 'f')
	{
		load_file("f.txt", str);
	}
	else if (x == 'g')
	{
		load_file("g.txt", str);
	}
	else if (x == 'h')
	{
		load_file("h.txt", str);
	}
	else if (x == 'i')
	{
		load_file("i.txt", str);
	}
	else if (x == 'j')
	{
		load_file("j.txt", str);
	}
	else if (x == 'k')
	{
		load_file("k.txt", str);
	}
	else if (x == 'l')
	{
		load_file("l.txt", str);
	}
	else if (x == 'm')
	{
		load_file("m.txt", str);
	}
	else if (x == 'n')
	{
		load_file("n.txt", str);
	}
	else if (x == 'o')
	{
		load_file("o.txt", str);
	}
	else if (x == 'p')
	{
		load_file("p.txt", str);
	}
	else if (x == 'q')
	{
		load_file("q.txt", str);
	}
	else if (x == 'r')
	{
		load_file("r.txt", str);
	}
	else if (x == 's')
	{
		load_file("s.txt", str);
	}
	else if (x == 't')
	{
		load_file("t.txt", str);
	}
	else if (x == 'u')
	{
		load_file("u.txt", str);
	}
	else if (x == 'v')
	{
		load_file("v.txt", str);
	}
	else if (x == 'w')
	{
		load_file("w.txt", str);
	}
	else if (x == 'x')
	{
		load_file("x.txt", str);
	}
	else if (x == 'y')
	{
		load_file("y.txt", str);
	}
	else if (x == 'z')
	{
		load_file("z.txt", str);
	}
	else if (isdigit(x)) // Number
	{
		load_file("numbers.txt", str);
	}
	else if (ispunct(x)) // Special character
	{
		load_file("specialChar.txt", str);
	}
}