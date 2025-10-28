#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#define MAXLINE 100
#define MAXVALUES 50

void display(std::vector<int>& thisData);

void display(std::vector<int>& thisData) {
    for (auto x : thisData) {
        std::cout << x << "\n";
    }
}

int main(int argc, char **argv) {
    std::ifstream inData(argv[1]);
    //validate file opened without problems
    if(inData.fail()) {
        std::cout << "Error opening file.\n";
        return 0;
    }
    std::vector<int> myData;

    char buffer[MAXLINE];
    int x = 0;
    while((inData >> buffer) && x < MAXVALUES) {
        //validate for numbers only
        if (buffer[0] < '0' || buffer[0] > '9') {
            std::cout << "Only positive numbers allowed!\n";
            return 0;
        }
        //convert string to int (atof for double)
        myData.push_back(atoi(buffer));
        x++;
    }
    std::cout << "Data vector size: " << myData.size() << " and capacity: " << myData.capacity() << "\n";
    if(myData.size())
        std::cout << "Unsorted:\n";
    display(myData);
}