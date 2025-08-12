/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //While loop that goes until the end of both list nodes are reached
        bool end1 = false;
        bool end2 = false;
        ListNode *temp2 = new ListNode; /*might not need "*"*/
        ListNode *root = temp2; /*might not need "*"*/
        int temp = 0;
        while(!end1 || !end2) {
            temp = 0;
            //L1
            if(!end1) { //still have nodes left
                temp2->val += l1->val;
                if(!(l1->next))
                    end1 = true;
                else
                    l1 = l1->next;
            }
            //L2
            if(!end2) { //still have nodes left
                temp2->val += l2->val;
                if(!(l2->next))
                    end2 = true;
                else
                    l2 = l2->next;
            }
            //Assign value
            if(temp2->val >= 10) {
                temp2->val = temp2->val - 10;
                temp = 1;
            }
            if(!(end1 && end2) || temp) {
                temp2->next = new ListNode;
                temp2 = temp2->next;
                temp2->val += temp;
            }
        }
        return root;
    }
};