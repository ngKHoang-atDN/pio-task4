#include <bits/stdc++.h>
using namespace std ;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if  ( root == nullptr )return true;
        return dfs(root->left,root->right);
    }
private:
    bool dfs(TreeNode *a,TreeNode *b) {
        if ( a ==  nullptr and b == nullptr ) return true ;
        if  ( a ==  nullptr or b == nullptr ) return false ;
        if ( a->val == b->val) {
            return dfs(a->left,b->right) and dfs(a->right,b->left); 
        }
        else return false ;
    }
}; 