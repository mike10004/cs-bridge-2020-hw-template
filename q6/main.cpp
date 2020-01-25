#include <iostream>
#include <string>

using namespace std;

const int WEEKDAY_RATE_CENTS_PER_MINUTE = 40;
const int WEEKNIGHT_RATE_CENTS_PER_MINUTE = 25;
const int WEEKEND_RATE_CENTS_PER_MINUTE = 15;

int main()
{
    string dayOfWeek;
    int callStartHours, callStartMinutes;
    char callTimeColon;
    int callDurationMinutes;
    cout << "Enter day of week call was started: ";
    cin >> dayOfWeek;
    cout << "Enter time of day call was started (24-hour format): ";
    cin >> callStartHours >> callTimeColon >> callStartMinutes;
    cout << "Enter length of call in minutes: ";
    cin >> callDurationMinutes;
    
    int callCostCents;
    if (dayOfWeek == "Sa" || dayOfWeek == "Su") {
        callCostCents = callDurationMinutes * WEEKEND_RATE_CENTS_PER_MINUTE;
    } else {
        // starts strictly before 08:00 or after 18:00: weekday rate
        if (callStartHours < 8 
                || callStartHours > 18 
                || (callStartHours == 18 && callStartMinutes > 0)) {
            callCostCents = callDurationMinutes * WEEKNIGHT_RATE_CENTS_PER_MINUTE;
        } else {
            callCostCents = callDurationMinutes * WEEKDAY_RATE_CENTS_PER_MINUTE;
        }
    }    
    cout << "Cost of call: " << (callCostCents / 100) 
         << " dollars and " << (callCostCents % 100) << " cents" << endl;
    return 0;
}
