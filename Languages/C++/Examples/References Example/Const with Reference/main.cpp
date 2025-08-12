/*
    Basically the same as pass by reference except
    parameters aren't allowed
*/

#include <iostream>

int square(int const &i) {

  return i * i;

}

int main() {
  
  int side = 5;
  
  std::cout << square(side) << "\n";

}