#include <iostream>
#include <list>
#include <fstream>
using namespace std;

int main() {
	fstream file("listB.txt", ios::out);
	list<int> A, B;
	int temp;
	cin >> temp;

   
	while (temp > 0) {
		A.push_back(temp);
		B.push_front(temp);
		cin >> temp;
	}

   
	for (list<int>::iterator it = A.begin(); it != A.end(); it++) {
		if (it == A.begin())
			cout << *it;
		else cout << " " << *it;
	}

    
	if (file.good() && file.is_open()) {
		for (list<int>::iterator it = B.begin(); it != B.end(); it++) {
			if (it == B.begin())
                file << *it;
			else file << " " << *it;
		}
	} else cout << "Error while opening file!" << endl;

	file.close();

   cout << endl;

    temp = *A.begin();
    A.push_back(temp);
    A.pop_front();

    
    temp = *B.begin();
    B.push_back(temp);
    B.pop_front();

    for (list<int>::iterator it = A.begin(); it != A.end(); it++) {
		if (it == A.begin())
			cout << *it;
		else cout << "," << *it;
	}
    cout << endl;

    
    for (list<int>::iterator it = B.begin(); it != B.end(); it++) {
		if (it == B.begin())
			cout << *it;
		else cout << "," << *it;
	}

    cout <<  endl;

    
    A.merge(B);
    A.sort();

   
    for (list<int>::iterator it = A.begin(); it != A.end(); it++) {
		if (it == A.begin())
			cout << *it;
		else cout << " " << *it;
	}

	cout << endl;

	return 0;
}