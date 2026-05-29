#include <iostream>
using namespace std;

int main() {
    int num, reversed = 0;

    cout << "Enter a number: ";
    cin >> num;

    int temp = num;  // Save original

    // Reverse the number
    while (temp != 0) {
        int lastDigit = temp % 10;
        reversed = reversed * 10 + lastDigit;
        temp = temp / 10;
    }

    // Check palindrome
    if (num == reversed) {
        cout << num << " is a Palindrome!" << endl;
    } else {
        cout << num << " is NOT a Palindrome!" << endl;
    }

    return 0;
}