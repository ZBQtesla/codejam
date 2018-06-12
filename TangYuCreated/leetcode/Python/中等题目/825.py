class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        
        ans = 0
        for i in range(15, 121):
            if cnt[i] == 0: continue
            for j in range(int(i*0.5+7)+1, i):
                ans += cnt[i] * cnt[j]
            ans += (cnt[i])*(cnt[i]-1)
        return ans
