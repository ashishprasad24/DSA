string sort(string s){
    vector <int>alpha(26,0);
    
    for(int i=0;i<s.size();i++)
    {
        alpha[s[i]-'a']++;
        
    }
    string ans;
    
    for(int i=0;i<26;i++)
    {
        char c='a'+i;
        while(alpha[i])
        {
            ans+=c;
            alpha[i]--;
        }
        
    }
    return ans;
}
