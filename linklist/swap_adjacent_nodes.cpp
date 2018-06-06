#include <iostream>
using namespace std;

/**
 * C++11
 * 给定一个链表，交换每两个相邻结点并返回其链表头
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
    list = list->next;
    list->next = new ListNode(1);
    return head;
}

ListNode* swap(ListNode* head){
    if (head == nullptr || head->next == nullptr){
        return head;
    }
    
    ListNode* prev;
    ListNode* curr;
    ListNode* next, *tmp;
    ListNode* nhead;
    tmp = head;
    curr = head->next;
    prev = head;
    nhead = curr;
    while (curr->next && curr->next->next){
        next = curr->next;
        prev->next = next;
        curr->next = prev;
        tmp = prev;
        prev = next;
        curr = next->next;
    }
    //cout<<tmp->val<<" "<<curr->val<<" "<<prev->val<<endl;
    tmp->next = curr;
    tmp = curr->next;
    curr->next = prev;
    prev->next = tmp;
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
    cout<<"after swap"<<endl;
    ListNode* nhead = swap(list);
    echo(nhead);
    return 0;
}

