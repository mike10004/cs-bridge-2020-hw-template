#include <iostream>

using namespace std;

const int FLOOR_ROUND = 1;
const int CEILING_ROUND = 2;
const int ROUND = 3;

int main()
{
    double inputNumber;
    int truncatedNumber;
    int roundedNumber;
    int roundingMethod;
    cout << "Please enter a Real number:\n";
    cin >> inputNumber;
    cout << "Choose your rounding method:\n"
         << "1. Floor round\n"
         << "2. Ceiling round\n"
         << "3. Round to the nearest whole number\n";
    cin >> roundingMethod;
    truncatedNumber = (int) inputNumber;
    if (truncatedNumber == inputNumber) {
        roundedNumber = truncatedNumber;
    } else {
        switch (roundingMethod) {
            case FLOOR_ROUND:
                roundedNumber = truncatedNumber;
                if (inputNumber < 0) {
                    roundedNumber = roundedNumber - 1;
                }
                break;
            case CEILING_ROUND:
                roundedNumber = truncatedNumber;
                if (inputNumber > 0) {
                    roundedNumber = roundedNumber + 1;
                }
                break;
            case ROUND:
                if (inputNumber < 0) {
                    roundedNumber = (int) (inputNumber - 0.5);
                } else {
                    roundedNumber = (int) (inputNumber + 0.5);
                }
                break;
            default:
                cout << "Choice " << roundingMethod << " is invalid\n";
                return 1;
        }
    }
    cout << roundedNumber << endl;
    return 0;
}
