#include <iostream>

int main() {
    //double, 8 bytes, 1.5 × 10^−45 to 3.4 × 10
    //float, 4 bytes
    double num;
    std::cout << "Enter a positive double: ";
    while (!(std::cin >> num) || num <= 0)
    {
        std::cout << "ERROR: a positive double must be entered: ";
        std::cin.clear();
        std::cin.ignore(1000, '\n');
    }
    std::cout << "Your double is: " << num << "\n";
}