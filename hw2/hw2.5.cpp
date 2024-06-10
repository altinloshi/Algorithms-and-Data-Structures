#include <iostream>
#include <cstdlib>
#include <set>
using namespace std;
int main() {
	// Set is the suitable container
	int temp;
	set<int> randoms;
	set<int>::iterator it;

	// Initializing random number generator
	srand(time(NULL));

	// Produce random numbers until 6 unique ones show up and insert them into
	// the set
	while (randoms.size() != 6) {
		temp = rand() % 49 + 1;
		randoms.insert(temp);
	}

	// Iterate through the set and output each integer into stdout
	for (it = randoms.begin(); it != randoms.end(); it++) {
		if (it == randoms.begin())
			cout << *it;
		else cout << " " << *it;
	}
	cout << endl;

	return 0;
}