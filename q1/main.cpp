#include <iostream>
#include <string>

using namespace std;

const double CLUB_CARD_DISCOUNT = 0.1;  // 10% off

int main()
{
    string clubCardAnswer;
    double item1Price, item2Price;
    double minItemPrice, maxItemPrice;
    double taxPercent, taxMultiplier;
    double priceBase, priceAfterDiscount, priceTotal;

    cout << "Enter price of first item: ";
    cin >> item1Price;
    cout << "Enter price of second item: ";
    cin >> item2Price;
    cout << "Does customer have a club card? (Y/N): ";
    cin >> clubCardAnswer;
    cout << "Enter tax rate, e.g. 5.5 for 5.5% tax: ";
    cin >> taxPercent;

    minItemPrice = item1Price;
    maxItemPrice = item2Price;
    if (item1Price > item2Price)
    {
        maxItemPrice = item1Price;
        minItemPrice = item2Price;
    }
    priceBase = item1Price + item2Price;
    priceAfterDiscount = maxItemPrice + (0.5 * minItemPrice);
    
    // interpret anything other than "yes"-like answers as "no"
    if (clubCardAnswer == "y" || clubCardAnswer == "Y" || clubCardAnswer == "yes")
    {
        priceAfterDiscount = priceAfterDiscount * (1.0 - CLUB_CARD_DISCOUNT);
    }
    taxMultiplier = 1.0 + (taxPercent / 100.0);
    priceTotal = priceAfterDiscount * taxMultiplier;

    // use 2 decimal places for all currency outputs
    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "Base price: " << priceBase << endl;
    cout << "Price after discounts: " << priceAfterDiscount << endl;
    cout << "Total price: " << priceTotal << endl;

    return 0;
}
