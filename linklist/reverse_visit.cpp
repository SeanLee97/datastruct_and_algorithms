#include <iostream>
#include <stack>
using namespace std;

/**
 * C++11
 * 倒叙访问链表
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

// 递归版本
void reverse(ListNode* head){
    if (head == nullptr)
        return;
    reverse(head->next);
    cout<<head->val<<" ";
}

// 结合栈来
void reverse_iter(ListNode* head){
    if (head == nullptr)
        return;
    stack<ListNode* >S;
    ListNode* tmp = head;
    while (tmp){
        S.push(tmp);
        tmp = tmp->next;
    }
    while (!S.empty()){
        tmp = S.top();
        cout<<tmp->val<<" ";
        S.pop();
    }
    cout<<endl;
}

void echo(ListNode* head){
    while (head){
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}

int main(void){
    ListNode* list = create_list();
    echo(list);
    cout<<"reverse visit"<<endl;
    reverse(list);
    cout<<endl;
    cout<<"非递归"<<endl;
    reverse_iter(list);
    return 0;
}

