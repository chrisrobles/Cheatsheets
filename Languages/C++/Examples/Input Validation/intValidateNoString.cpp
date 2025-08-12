#include <iostream>

int main() {
    //int, 4 bytes, -2147483648 to 2147483647
    //unsigned int, 4 bytes, 0 to 4294967295
    //short int, 2 bytes, -32768 to 32767
    //unsigned shoft int, 2 bytes, 0 to 65535
    //long int, 8 bytes, -2,147,483,648 to 2,147,483,647
    //unsigned long int, 8 bytes, 0 to 4,294,967,295
    //long long int
    //unsigned long long int
    int num;
    std::cout << "Enter a positive int: ";
    while (!(std::cin >> num) || num <= 0)
    {
        std::cout << "ERROR: a positive int must be entered: ";
        std::cin.clear();
        std::cin.ignore(1000, '\n');
    }
    std::cout << "Your int is: " << num << "\n";
}