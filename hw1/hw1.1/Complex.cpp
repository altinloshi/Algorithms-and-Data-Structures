#include <iostream>
#include <sstream>
#include "Complex.h"
 
using namespace std;

Complex::Complex(int Real, int Imaginary) {
    real = Real;
    imaginary = Imaginary;
}


Complex::Complex() {
    real = 0;
    imaginary = 0;
}


Complex::Complex(Complex& num) : real(num.real), imaginary(num.imaginary) {
}


Complex::~Complex() {
}


void Complex::setReal(int newReal) {
    real = newReal;
}

void Complex::setImaginary(int newImaginary) {
    imaginary = newImaginary;
}


int Complex::getReal() {
    return real;
}

int Complex::getImaginary() {
    return imaginary;
}

std::ostream& operator<<(std::ostream &out, const Complex &c) {
    if (c.imaginary >= 0)
        out << c.real << "+" << c.imaginary << "i";
	else out << c.real << c.imaginary << "i";
	return out;
}

std::istream& operator>>(std::istream& in, Complex &c) {
	string delimiter = "+-";
    std::string number;
    std::getline(in, number);
    
    std::size_t found = number.find_last_of(delimiter);

    std::string Real = number.substr(0, found);
    std::string Imaginary = number.substr(found, number.length() - 1);

    stringstream stringToIntRe(Real);
    stringToIntRe >> c.real;

    stringstream stringToIntIm(Imaginary);
    stringToIntIm >> c.imaginary;

    return in;
}

Complex Complex::operator+(const Complex& secondComplex) {
    Complex result((*this).real + secondComplex.real,
                   (*this).imaginary + secondComplex.imaginary);
	return result;
}

Complex Complex::operator-(const Complex& secondComplex) {
    Complex result((*this).real - secondComplex.real,
                   (*this).imaginary - secondComplex.imaginary);
    return result;
}

Complex Complex::operator*(const Complex& secondComplex) {
    Complex result((*this).real * secondComplex.real - 
                   (*this).imaginary * secondComplex.imaginary,
                   (*this).real * secondComplex.imaginary +
                   secondComplex.real * (*this).imaginary);
    return result;
}

Complex& Complex::operator=(const Complex obj) {
    real = obj.real;
    imaginary = obj.imaginary;
    return *this;
}

bool Complex::operator==(const Complex& obj) {
    if (this->real == obj.real && this->imaginary == obj.imaginary)
        return true;
    else return false;
}