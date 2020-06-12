class Solution {
public:
    vector<int> s;
    Solution(vector<int>& w) {
        std::ios_base::sync_with_stdio(false); 
        cin.tie(nullptr); cout.tie(nullptr);
        for (int ind : w){
            if(s.empty())
                s.push_back(ind);
            else
                s.push_back(ind + s.back());
        }
    }
    
    int pickIndex() {
        std::ios_base::sync_with_stdio(false); 
        cin.tie(nullptr); cout.tie(nullptr);
        int x = s.back();
        int index = rand() % x;
        auto it = upper_bound(s.begin(), s.end(),index);
        return it - s.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
