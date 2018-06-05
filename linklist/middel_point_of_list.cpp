#include <iostream>
using namespace std;

/**
 * C++11
 * 给定一个链表，编写一个函数以返回该链表结点的中间结点
 * 思路：runner & chaser
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

ListNode* middle_point(ListNode* head){
    if (head == nullptr)
        return nullptr;
    ListNode* chaser = head;
    ListNode* runner = head;
    while (runner->next && runner->next->next){ // 注意开始条件是runner->next
        runner = runner->next->next;
        chaser = chaser->next;
    }
    return chaser;
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
    cout<<"middle node"<<endl;
    ListNode* mid_node = middle_point(list);
    cout<<mid_node->val<<endl;
    return 0;
}

