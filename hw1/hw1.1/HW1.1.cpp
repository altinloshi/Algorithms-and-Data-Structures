#include <iostream>
#include "Complex.h"


template <class T>
int array_search(T arr[], int length, T element) {
	for (int i = 0; i < length; i++)
		if (arr[i] == element)
			return i;
	return -1;
}

int main() {
	
	int i = 372;
	int iArr[10] = {-7, 4, 2, 5, 19, 28, -4, 0, 372, 11};

	double d = 8.41;
    double dArr[8] = {1.8, 2.4, 12.2, -0.4, 5.4, 8.4, 8.41, -2.5};

	std::string s = "search";
	std::string sArr[3] = {"Ay", "Here", "Elements"};

	Complex c(-4,-3);
	Complex c1(6,-1), c2(0,2), c3(-4,-3), c4(2,5);
    Complex cArr[]={c1, c2, c3, c4};

	std::cout << "Search for integer " << i << " in int array gives index: "
			  << array_search(iArr, 10, i)
			  << std::endl;
	std::cout << "Search for double " << d << " in double array gives index: "
			  << array_search(dArr, 8, d)
			  << std::endl;
	std::cout << "Search for string " << s << " in string array gives index: "
			  << array_search(sArr, 3, s)
			  << std::endl;
	std::cout << "Search for Complex " << c << " in Complex array gives index: "
			  << array_search(cArr, 4, c)
			  << std::endl;

	return 0;
}