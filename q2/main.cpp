#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    int graduationYear, currentYear, yearsRemaining;
    string status;

    cout << "Please enter your name: ";
    cin >> name;
    cout << "Please enter your graduation year: ";
    cin >> graduationYear;
    cout << "Please enter current year: ";
    cin >> currentYear;

    yearsRemaining = graduationYear - currentYear;
    switch (yearsRemaining)
    {
        case 1:
            status = "a Senior";
            break;
        case 2:
            status = "a Junior";
            break;
        case 3:
            status = "a Sophomore";
            break;
        case 4:
            status = "a Freshman";
            break;
        default:
            if (yearsRemaining <= 0) {
                status = "graduated";
            } else {
                status = "not in college yet";
            }
    }

    cout << name << ", you are " << status << endl;
    return 0;
}
