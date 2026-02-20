class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        bool flag = true;
        while (stones.size() > 1) {
            if (flag)
                sort(stones.begin(), stones.end());
            flag = true;
            int s = stones.size();
            int res = stones[s-1] - stones[s-2];
            stones.erase(stones.end()-1);
            if (res != 0)
                stones[s-2] = res;
            else {
                stones.erase(stones.end()-1);
                flag = false;
            }
        }
        if (stones.size() == 1)
            return stones[0];
        else
            return 0;
    }
};