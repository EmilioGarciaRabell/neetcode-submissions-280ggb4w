class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size()){
            return false;
        }
        
        std::unordered_map<char, int> charCountS1;
        std::unordered_map<char, int> charCountS2;

        for (char c = 'a'; c <= 'z'; ++c) {
            charCountS1[c] = 0;
            charCountS2[c] = 0;
        }

        for (int i = 0; i < s1.size(); i++){
            charCountS1[s1[i]] ++;
        }

        int l = 0;
        for (int r = 0; r < s2.size(); r++){
            charCountS2[s2[r]] ++;

            if (charCountS1 == charCountS2){
                return true;
            }else if((r - l + 1) >= s1.size()){
                charCountS2[s2[l]] --;
                l ++;
            }
        }

        return false;
    }
};
