#include <iostream>
#include <stack>
#include <queue>
using namespace std;

/**
 * 二叉树相关操作
 * 遍历：前序、中序、后序、层序的递归和非递归方式实现
 * 树的深度：递归及非递归方式
 * 二叉树的镜像
 */

typedef int datatype;
struct BTNode{
    datatype data;
    struct BTNode* left, *right;
};

/**
 * 求树的深度
 */

// 递归方式
int depth(BTNode* pRoot){
    if (pRoot == NULL)
        return 0;
    int left = depth(pRoot->left);
    int right = depth(pRoot->right);
    return left > right ? left +1 : right + 1;
}

// 非递归方式：使用中序非递归方式遍历实现
int depth_iter(BTNode* pRoot){
    if (pRoot == NULL)
        return 0;
    int curr_depth = 1;
    int max_depth = -1;
    stack<BTNode* >S1;
    stack<int>S2;
    BTNode* p;
    p = pRoot;
    while (p!=NULL || !S1.empty()){
        while (p!=NULL){
            S1.push(p);
            S2.push(curr_depth);    
            p = p->left;
            curr_depth++;
        }
        p = S1.top();
        S1.pop();
        curr_depth = S2.top();
        S2.pop();
        if (p->left == NULL && p->right == NULL){
            // 叶子结点的时候更新
            max_depth = curr_depth > max_depth ? curr_depth : max_depth;
        }
        p = p->right;
        curr_depth++;
    }
    return max_depth;
}

/**
 * 前序遍历
 */

// 递归方式
void preorder(BTNode* pRoot){
    if (pRoot != NULL){
        cout<<pRoot->data<<" ";
        preorder(pRoot->left);
        preorder(pRoot->right);
    }
}

// 非递归方式
// 采用辅助栈实现
void preorder_iter(BTNode* pRoot){
    if (pRoot != NULL){
        BTNode* p;
        p = pRoot;
        stack<BTNode *> S;
        S.push(p);
        while (! S.empty()){
            p = S.top();
            S.pop();
            while (p != NULL){
                cout<<p->data<<" ";
                if (p->right != NULL){
                    // 压栈
                    S.push(p->right);
                }
                p = p->left;
            }
        }
    }
}

/**
 * 中序遍历
 */

// 递归方式
void inorder(BTNode* pRoot){
    if (pRoot != NULL){
        inorder(pRoot->left);
        cout<<pRoot->data<<" ";
        inorder(pRoot->right);
    }
}

// 非递归方式
void inorder_iter(BTNode* pRoot){
    if (pRoot != NULL){
        BTNode* p;
        p = pRoot;
        stack<BTNode *>S;
        while (p || !S.empty()){
            while (p){
               S.push(p);
               p = p->left;
            }
            p = S.top();
            S.pop();
            cout<<p->data<<" ";
            p = p->right;
        }
    }
}


/**
 * 后序遍历
 */

// 递归方式
void postorder(BTNode* pRoot){
    if (pRoot != NULL){
        postorder(pRoot->left);
        postorder(pRoot->right);
        cout<<pRoot->data<<" ";
    }
} 

// 非递归方式，较前两种负责，需要添加标志位
struct sdata{
    BTNode* q;
    int tag;
};

void postorder_iter(BTNode* pRoot){
    if (pRoot != NULL){
        BTNode* p;
        p = pRoot;
        sdata* sd;
        int tag;
        stack<sdata*>S;
        do {
            while (p != NULL){
                sd = new sdata;
                sd->q = p;
                sd->tag = 0;
                S.push(sd);
                p = p->left;
            }
            sd = S.top();
            S.pop();
            p = sd->q;
            tag = sd->tag;
            if (tag == 0){
                sd->q = p;
                sd->tag = 1;
                S.push(sd);
                p = p->right;
            }else{
                cout<<p->data<<" ";
                p = NULL; // 访问后必须置NULL，否则将陷入死循环
            }
        }while (p != NULL || !S.empty());
    } 
}

/**
 * 层序遍历
 */
// 递归方式：递归方式相比非递归方式要复杂
void _layerorder(BTNode* pRoot, int level){
    if (pRoot == NULL || level < 0)
        return;
    if (level == 1)
        cout<<pRoot->data<<" ";

    if (pRoot->left)
        _layerorder(pRoot->left, level-1);
    if (pRoot->right)
        _layerorder(pRoot->right, level-1);
}

void layerorder(BTNode* pRoot){
    if (pRoot == NULL)
        return;
    int d = depth_iter(pRoot);
    // 逐层输出
    for (int level=1; level<=d; level++){
        _layerorder(pRoot, level);
    }
}


// 非递归方式:采用辅助队列实现
void layerorder_iter(BTNode* pRoot){
    if (pRoot != NULL){
        BTNode* p;
        p = pRoot;
        queue<BTNode*>Q;
        Q.push(p);
        while (! Q.empty()){
            p = Q.front();
            cout<<p->data<<" ";
            Q.pop();
            if (p->left != NULL)
                Q.push(p->left);
            if (p->right != NULL)
                Q.push(p->right);
        }
    }
}

/**
 * 求二叉树的镜像
 */
void mirror(BTNode* pRoot){
    if (pRoot == NULL)
        return;
    BTNode* t;
    t = pRoot->left;
    pRoot->left = pRoot->right;
    pRoot->right = t;
    mirror(pRoot->left);
    mirror(pRoot->right);
}

// 创建二叉树
BTNode* create(){
    BTNode* pRoot = new BTNode;
    pRoot->data = 1;
    pRoot->left = new BTNode;
    pRoot->left->data = 2;
    pRoot->right = new BTNode;
    pRoot->right->data = 3;
    pRoot->left->left = new BTNode;
    pRoot->left->left->data = 4;
    pRoot->left->right = new BTNode;
    pRoot->left->right->data = 5;
    return pRoot;
}

int main(void){
    BTNode* pRoot = create();
    BTNode* p;
    // 树的深度
    int d;
    cout<<"递归树的深度"<<endl;
    p = pRoot;
    d = depth(pRoot);
    cout<<d<<endl;
    cout<<"非递归树的深度"<<endl;
    p = pRoot;
    d = depth_iter(pRoot);
    cout<<d<<endl;
    // 前序遍历
    cout<<"递归前序遍历"<<endl;
    p = pRoot;
    preorder(p);
    cout<<endl;
    cout<<"非递归前序遍历"<<endl;
    p = pRoot;
    preorder_iter(p);
    cout<<endl;

    // 中序遍历
    cout<<"递归中序遍历"<<endl;
    p = pRoot;
    inorder(p);
    cout<<endl;
    cout<<"非递归中序遍历"<<endl;
    inorder_iter(p);
    cout<<endl;

    // 后序遍历
    cout<<"递归后序遍历"<<endl;
    p = pRoot;
    postorder(p);
    cout<<endl;
    cout<<"非递归后序遍历"<<endl;
    p = pRoot;
    postorder_iter(p);
    cout<<endl;

    // 层序遍历
    cout<<"递归层序遍历"<<endl;
    p = pRoot;
    layerorder(p);
    cout<<endl;
    cout<<"非递归层序遍历"<<endl;
    p = pRoot;
    layerorder_iter(p);
    cout<<endl;

    // 求二叉树的镜像
    p = pRoot;
    mirror(p);
    cout<<"二叉树的镜像"<<endl;
    layerorder_iter(p);
    cout<<endl;

    return 0;
} 
