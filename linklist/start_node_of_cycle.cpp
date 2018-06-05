#include <iostream>
using namespace std;

/**
 * C++11
 * 给定一个可能包含一个环的链表，编写一个函数来返回环开始的结点。如果该链表不包含环返回NULL
 * 思路：runner & chaser,runner以两倍速前进，chaser以一倍速度前进,在有环的情况下runner与chaser
 * 一定在某点相遇。相遇后再让chaser从头结点出发再次追赶runner，此时都以一倍速前进，当两者第二次相遇时即为环
 * 开始的位置.
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
    ListNode* nlist = list->next;  // 环
    nlist->next = list;
    return head;
}

ListNode* find_start_node(ListNode* head){
    ListNode* runner = head;
    ListNode* chaser = head;
    
    while (runner && runner->next){
        chaser = chaser->next;
        runner = runner->next->next;
        if (chaser == runner)
            break;
    }

    if (runner == nullptr || runner->next == nullptr)
        return nullptr;
    
    chaser = head;
    while (chaser != runner){
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
    //echo(list);
    cout<<"start node"<<endl;
    ListNode* start_node = find_start_node(list);
    cout<<start_node->val<<endl;
    return 0;
}

