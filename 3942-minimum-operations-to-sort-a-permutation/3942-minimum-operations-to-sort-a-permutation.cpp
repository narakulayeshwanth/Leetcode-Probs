class Solution {
    public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int pos0 = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                pos0 = i;
                break;
            }
        }
        bool canAsc = true;
        for (int i = 0; i < n; i++) {
            if (nums[(pos0 + i) % n] != i) {
                canAsc = false;
                break;
            }
        }
        bool canDesc = true;
        for (int i = 0; i < n; i++) {
            if (nums[(pos0 - i + n) % n] != i) {
                canDesc = false;
                break;
            }
        }
        int ans = 1e9;
        if (canAsc) {
            ans = min(ans, pos0);
            ans = min(ans, (n - pos0) % n + 2);
        }
        if (canDesc) {
            ans = min(ans, (pos0 + 1) % n + 1);
            ans = min(ans, (n - 1 - pos0) + 1);
        }
        return ans >= 1e9 ? -1 : ans;
    }
};