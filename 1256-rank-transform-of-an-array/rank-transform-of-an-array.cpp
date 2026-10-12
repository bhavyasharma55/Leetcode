class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> b = arr;
        sort(b.begin(), b.end());
        unordered_map<int,int> m;
        for (int x : b) if (!m.count(x)) m[x] = m.size() + 1;
        for (int &x : arr) x = m[x];
        return arr;
    }
};