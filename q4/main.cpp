#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double inputNumber, roundedNumber;
    int roundingMethod;
    cout << "Please enter a Real number:\n";
    cin >> inputNumber;
    cout << "Choose your rounding method:\n"
         << "1. Floor round\n"
         << "2. Ceiling round\n"
         << "3. Round to the nearest whole number\n";
    cin >> roundingMethod;
    switch (roundingMethod)
    {
        case 1:
            roundedNumber = floor(inputNumber);
            break;
        case 2:
            roundedNumber = ceil(inputNumber);
            break;
        case 3:
            roundedNumber = round(inputNumber);
            break;
        default:
            cout << "Choice " << roundingMethod << " is invalid\n";
            return 1;
    }
    cout << roundedNumber << endl;
    return 0;
}
