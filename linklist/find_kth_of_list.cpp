#include <iostream>
using namespace std;

/**
 * C++11
 * 找到一个单向链表中，距离最后一个元素为k的那个元素
 * 思路：runner & chaser， runner要提前chaser走k步，然后两者以相同的倍速前进
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

ListNode* find_kth_node(ListNode* head, int k){
    if (head == nullptr)
        return nullptr;
    ListNode* chaser = head;
    ListNode* runner = head;

    while (--k && runner){
         runner = runner->next;
    }
    while (runner->next){
        chaser = chaser->next;
        runner = runner->next;
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
    ListNode* kth_node = find_kth_node(list, 3);
    cout<<kth_node->val<<endl;
    return 0;
}

