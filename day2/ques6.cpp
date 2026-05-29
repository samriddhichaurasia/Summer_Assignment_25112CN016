#include <iostream>
using namespace std;

int main() {
    int num, reversed = 0;

    cout << "Enter a number: ";
    cin >> num;

    int temp = num;

    while (temp != 0) {
        int lastDigit = temp % 10;          // Get last digit
        reversed = reversed * 10 + lastDigit; // Build reversed number
        temp = temp / 10;                   // Remove last digit
    }

    cout << "Reversed number: " << reversed << endl;

    return 0;
}