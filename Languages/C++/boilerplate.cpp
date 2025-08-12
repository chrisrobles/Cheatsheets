#include <iostream>

using namespace std;

int main() {
    cout << "Hello World!" << endl;
    int x = 0;
    int &y = x;
    int const * const xy = &x;

    cout << xy << " " << &y;
    return 0;
}