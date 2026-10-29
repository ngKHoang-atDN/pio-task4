#include <bits/stdc++.h>
using namespace std ;

class Solution {
public  :
    string longestCommonPrefix(vector<string>& strs) {
        if ( strs.empty() ) return output ;
        for ( int i = 0 ; i < strs[0].length(); i++ ) { 
            output += (strs[0][i]);
            for(int j = 1 ; j < strs.size() ; j++ ) {
                if (  ( strs[j].size() <= i  )  or  ( strs[j][i] != output[i]  ) ) {
                    return output.substr(0,i);
                }
            }
        }
        return output;
    }
private : 
    string output ="";
};
