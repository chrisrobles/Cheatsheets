int lengthOfLongestSubstring(string s) {
    vector<int> dict(256, -1);
    int maxLen = 0, start = -1;
    for (int i = 0; i != s.length(); i++) {
        if (dict[s[i]] > start) //collision
            start = dict[s[i]]; //set the next collision location to right
        dict[s[i]] = i; //set the character location with where it was found
        maxLen = max(maxLen, i - start); //check longest substring from previous and from start to now
    }
    return maxLen;
}