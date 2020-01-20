#include <iostream>

using namespace std;

const int CENTS_PER_QUARTER = 25;
const int CENTS_PER_DIME = 10;
const int CENTS_PER_NICKEL = 5;
const int CENTS_PER_PENNY = 1;

int main()
{
    int n_quarters, n_dimes, n_nickels, n_pennies;
    cout << "Please enter number of coins:\n";
    cout << "# of quarters: "; 
    cin >> n_quarters;
    cout << "# of dimes: "; 
    cin >> n_dimes;
    cout << "# of nickels: "; 
    cin >> n_nickels;
    cout << "# of pennies: "; 
    cin >> n_pennies;
    int total_cents = (n_quarters * CENTS_PER_QUARTER)
            + (n_dimes * CENTS_PER_DIME)
            + (n_nickels * CENTS_PER_NICKEL)
            + (n_pennies * CENTS_PER_PENNY);
    int n_dollars = total_cents / 100;
    int cents_remaining = total_cents % 100;
    cout << "The total is " << n_dollars << " dollars and " << cents_remaining << " cents\n";
    return 0;
}
