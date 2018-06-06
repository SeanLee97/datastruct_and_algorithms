#include <iostream>
using namespace std;

struct AdjListNode{
    int val;
    AdjListNode *next;
    AdjListNode(int val):val(val), next(nullptr){}
};

struct AdjList{
    AdjListNode *head;
    AdjList():head(nullptr){}
};

template<int vsize, bool bidirection=false>
class Graph{
public:
    Graph(){
        this->list = new AdjList[vsize];
    }
    void addEdge(int src, int tgt);
    void printGraph();
    virtual ~Graph(){
        delete[] list;
    }

private: 
    // 邻接表
    AdjList *list;
};

template<int vsize, bool bidirection>
void Graph<vsize, bidirection>::addEdge(int src, int tgt){
    AdjListNode* node = new AdjListNode(tgt);
    node->next = this->list[src].head;
    this->list[src].head = node;
    if (bidirection){
        node = new AdjListNode(src);
        node->next = this->list[tgt].head;
        this->list[tgt].head = node;
    } 
}

template<int vsize, bool bidirection>
void Graph<vsize, bidirection>::printGraph(){
    for (int i=0; i<vsize; i++){
        AdjListNode *root = this->list[i].head;
        cout<<"Adjacent list of vertex "<<i<<endl;
        while (root != nullptr){
            cout<<root->val<<" -> ";
            root = root->next;
        }
        cout<<endl;
    }
}


int main(void){
    Graph<4, false>*graph = new Graph<4, false>();
    graph->addEdge(0, 1);
    graph->addEdge(0, 2);
    graph->addEdge(0, 3);
    graph->addEdge(1, 3);
    graph->addEdge(2, 3);    

    graph->printGraph();
    delete graph;
    return 0;
}
