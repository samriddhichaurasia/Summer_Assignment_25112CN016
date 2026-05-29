#include <iostream>
using namespace std;

int main() {
    int num, sum = 0;

    cout << "Enter a number: ";
    cin >> num;

    int temp = num;  // Save original number

    while (temp != 0) {
        int lastDigit = temp % 10;  // Extract last digit
        sum += lastDigit;           // Add to sum
        temp = temp / 10;           // Remove last digit
    }

    cout << "Sum of digits of " << num << " = " << sum << endl;

    return 0;
}