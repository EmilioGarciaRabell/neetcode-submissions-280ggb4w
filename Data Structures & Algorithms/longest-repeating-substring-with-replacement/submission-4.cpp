class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_len = 0;
        int l = 0;
        int n = s.size();
        std::unordered_map<char,int> frequencies;
        int max_freq = 0;
        for(int r = 0; r < n;  r++){
            frequencies[s[r]] ++;
            max_freq = std::max<int>(max_freq, frequencies[s[r]]);
            
            while (((r - l + 1) - max_freq) > k){
                frequencies[s[l]] --;
                l ++;
                
            }

            max_len = std::max<int>(max_len, r - l + 1);

        }
        return max_len;
    }
};
