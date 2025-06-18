#include <iostream>

class Song {
    std::string title;
    std::string artist;

    public:
        int test = 302;
        Song(std::string new_title, std::string new_artist);
        void getName();
};