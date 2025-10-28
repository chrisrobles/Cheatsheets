#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
std::string str = "Ben";
int main ()
{
    str = 35;
    std::cout << str << std::endl;
    /*ListNode *test;
    test = new ListNode;
    test->val = 5;*/
    std::string s = "test";
    std::vector<int> dict(256, -1);
    //dict[s[0]];
    std::cout << dict[s[0]] << std::endl;
    return 0;
}