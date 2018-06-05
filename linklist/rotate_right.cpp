#include <iostream>
using namespace std;

/**
 * C++11
 * 给定一个链表，向右旋转链表k个位置（k>=0）
 * 思路：runner & chaser， 假设链表长度为len则runner要先走len-k-1步，接着以同样速率前进当runner到达终点则chaser到达旋转点
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

ListNode* rotate(ListNode* head, int k){
    if (head == nullptr)
        return nullptr;

    ListNode* chaser = head;
    ListNode* runner = head;
    ListNode* curr = head;
    int len = 0;
    
    while (curr){
        curr = curr->next;
        len++;
    }
    
    len = len-k;
    if (len < 0)
        return nullptr;

    while (len-- && runner){
        runner = runner->next;
    }
    
    while (runner->next){
        chaser = chaser->next;
        runner = runner->next;
    }

    ListNode* nhead = chaser->next;
    chaser->next = nullptr;
    runner->next = head;
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
    cout<<"new list"<<endl;
    ListNode* nlist = rotate(list, 2);
    echo(nlist);
    return 0;
}

