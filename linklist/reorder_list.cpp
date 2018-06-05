#include <iostream>
using namespace std;

/**
 * C++11
 * 给定一个链表和一个值x，编写一个函数，对该链表重新排序，以便所有小于x的结点都出现在大于或等于x的结点前面
 * 思路：哑结点
 */
typedef int datatype;
struct ListNode{
    datatype val;
    ListNode *next;
    ListNode(datatype v):val(v), next(nullptr){}
};

ListNode* create_list(){
    ListNode* list = new ListNode(5);
    ListNode* head = list;
    list->next = new ListNode(6);
    list = list->next;
    list->next = new ListNode(3);
    list = list->next;
    list->next = new ListNode(2);
    return head;
}

ListNode* reorder_list(ListNode* head, datatype target){
    if (head == nullptr)
        return nullptr;
    ListNode* nhead = nullptr;
    ListNode* a_curr = new ListNode(0);
    ListNode* a_dummy = a_curr;  // 哑结点
    ListNode* b_curr = new ListNode(0);
    ListNode* b_dummy = b_curr;  // 哑结点

    while (head){
        ListNode* next = head->next;
        head->next = nullptr;
        if (head->val > target){
            b_curr->next = head;
            b_curr = head;
        }else{
            a_curr->next = head;
            a_curr = head;
        }
        head = next;
    }
    a_curr->next = b_dummy->next;
    nhead = a_dummy->next;
    
    delete a_dummy;
    delete b_dummy;

    return nhead;
}

void echo(ListNode* head){
    while (head){
        cout<<head->val<<endl;
        head = head->next;
    }
}

int main(void){
    ListNode* list = create_list();
    echo(list);
    cout<<"after reorder"<<endl;
    ListNode* nlist = reorder_list(list, 4);
    echo(nlist);
    return 0;
}

