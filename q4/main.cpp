#include <iostream>
#include <cmath>

using namespace std;

const int FLOOR_ROUND = 1;
const int CEILING_ROUND = 2;
const int ROUND = 3;

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
        case FLOOR_ROUND:
            roundedNumber = floor(inputNumber);
            break;
        case CEILING_ROUND:
            roundedNumber = ceil(inputNumber);
            break;
        case ROUND:
            roundedNumber = round(inputNumber);
            break;
        default:
            cout << "Choice " << roundingMethod << " is invalid\n";
            return 1;
    }
    cout << roundedNumber << endl;
    return 0;
}
