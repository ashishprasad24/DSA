class Solution {
public:
void paranth(int n,int left, int right,vector<string>&ans, string &temp)
{
    if (left+right==2*n)
    {
        ans.push_back(temp);
    }

    if(left<n)
    {
        temp.push_back('(');
        paranth(n,left+1,right,ans,temp);
        temp.pop_back();
    }

    if(right<left)
    {
        temp.push_back(')');
        paranth(n,left,right+1,ans,temp);
        temp.pop_back();
    }
}
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string temp;
        paranth(n,0,0,ans,temp);
        return ans;

        
    }
};
