#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a, b, c;      // These variable names are short but sensible for the context
    double x1, x2;       // The two possible solutions for x
    double discriminant;
    cout << "Please enter value of a: ";
    cin >> a;
    cout << "Please enter value of b: ";
    cin >> b;
    cout << "Please enter value of c: ";
    cin >> c;
    
    if (a != 0) {
        discriminant = (b * b) - (4 * a * c);
        if (discriminant < 0) {
            cout << "This equation has no real solution";
        } else {
            x1 = (-b + sqrt(discriminant)) / (2 * a);
            x2 = (-b - sqrt(discriminant)) / (2 * a);
            if (x1 == x2) {
                cout << "This equation has a single real solution x=" << x1;
            } else {
                cout << "This equation has two real solutions: x=" << x1 << " and x=" << x2;
            }
        }
    } else {
        if (b == 0) {
            if (c == 0) {
                cout << "This equation has an infinite number of solutions";
            } else {
                cout << "This equation has no solution";
            }
        } else {
            // a == 0 && b != 0 --> linear equation bx + c == 0 --> x = -c/b
            cout << "This equation has a single real solution x=" << (-c/b);
        }
    }
    cout << endl;
    return 0;
}
