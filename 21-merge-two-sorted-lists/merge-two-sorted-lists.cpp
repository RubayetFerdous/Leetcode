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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if (!list1){
            return list2;
        }
        if(!list2){
            return list1;
        }
        struct ListNode* tempp= new struct ListNode;
        struct ListNode& temp = *tempp;
        
        int val=list1->val;
        int val0=list2->val;

        if (val<val0){
            temp.val=val;
            list1=list1->next;

        }else {
            temp.val=val0;
            list2=list2->next;
        }
        temp.next=nullptr;
        temp.next=mergeTwoLists(list1,list2);

        return &temp;

        
    }
};