#include <iostream>

using namespace std;

const double BMI_MIDDLE_MIN_INCLUSIVE = 18.5;
const double BMI_MIDDLE_MAX_EXCLUSIVE = 25;
const double BMI_HIGH_MAX_EXCLUSIVE = 30;
const double KILOS_PER_POUND = 0.453592;
const double METERS_PER_INCH = 0.0254;

int main()
{
    double weightPounds, heightInches;
    double weightKilos, heightMeters;
    double bmi;
    
    cout << "Please enter weight (in pounds): ";
    cin >> weightPounds;
    cout << "Please enter height (in inches): ";
    cin >> heightInches;
    
    weightKilos = weightPounds * KILOS_PER_POUND;
    heightMeters = heightInches * METERS_PER_INCH;
    bmi = weightKilos / (heightMeters * heightMeters);

    cout << "The weight status is: ";
    if (bmi < BMI_MIDDLE_MIN_INCLUSIVE) {
        cout << "Underweight";
    } else if (bmi < BMI_MIDDLE_MAX_EXCLUSIVE) {
        cout << "Normal";
    } else if (bmi < BMI_HIGH_MAX_EXCLUSIVE) {
        cout << "Overweight";
    } else {
        cout << "Obese";
    }
    cout << endl;
    
    return 0;
}
