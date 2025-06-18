#include "song.hpp"
#include <iostream>

int main() {
    Song myFav("Somewhere Over the Rainbow", "Iz");
    myFav.getName();
    std::cout << myFav.test << std::endl;
}