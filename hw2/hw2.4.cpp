#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	vector<int> intArr;

	// Push integer values from 1 to 30
	for (int i = 1; i < 31; i++)
		intArr.push_back(i);
	intArr.push_back(5); // Push 5 at the end of the vector

	// Reverse the order of the integers in the vector
	reverse(intArr.begin(), intArr.end());

	// Iterate through the vector and print each integer
	for (vector<int>::iterator it = intArr.begin(); it != intArr.end();
		 it++) {
		if (it == intArr.begin())
			cout << *it;
		else cout << " " << *it;
	}
	cout << endl;

	// Replace every instance of the integer 5 with 129 in the vector
	replace(intArr.begin(), intArr.end(), 5, 129);

	// Iterate through the vector and print each integer
	for (vector<int>::iterator it = intArr.begin(); it != intArr.end();
		 it++) {
		if (it == intArr.begin())
			cout << *it;
		else cout << " " << *it;
	}
	cout << endl;

	return 0;
}