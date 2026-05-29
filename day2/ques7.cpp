#include <iostream>
using namespace std;

int main() {
    int num, product = 1;  // Start with 1, NOT 0!

    cout << "Enter a number: ";
    cin >> num;

    int temp = num;

    while (temp != 0) {
        int lastDigit = temp % 10;  // Extract last digit
        product *= lastDigit;        // Multiply to product
        temp = temp / 10;            // Remove last digit
    }

    cout << "Product of digits of " << num << " = " << product << endl;

    return 0;
}