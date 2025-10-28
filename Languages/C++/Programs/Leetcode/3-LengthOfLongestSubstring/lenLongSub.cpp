class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> arr (26);
        int index1 = 0;
        int index2 = 0;
        int length1 = 0;
        int length2 = 0;
        while (index1 < s.length()) {
            if(arr[(s[index1])] > 0) {//collision
                index2 = arr[(s[index1])]; //last index of the char
                arr.clear();
                index1 = index2;                
                if(length1 > length2) {//2nd + found collision
                    length2 = length1;
                }
                length1 = 1;
            }
            else {
                length1++;
            }
            arr[(s[index1])] = index1 + 1;
            index1++;
        }
        if (length1 > length2)
            length2 = length1;
        return length2;
    }
};