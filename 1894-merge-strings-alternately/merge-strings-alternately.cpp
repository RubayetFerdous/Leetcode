#include <string>
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string n="";
        int i;
        for (i=0;i<word1.size();i++){
            if (i==word2.size()){
                break;
            }else{
                n+=string(1,word1[i])+string(1,word2[i]);
            }
        }
        n+=word1.substr(i,word1.size())+word2.substr(i,word2.size());
        return n;
    }
};