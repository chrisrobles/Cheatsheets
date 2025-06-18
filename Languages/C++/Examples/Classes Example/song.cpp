#include "song.hpp"
#include <iostream>

Song::Song (std::string new_title, std::string new_artist) {
    title = new_title;
    artist = new_artist;
}

void Song::getName() {
    std::cout << title << " - " << artist << "\n";
}