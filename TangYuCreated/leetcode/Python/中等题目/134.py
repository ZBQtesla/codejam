class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for pos in range(len(gas)):
            gas[pos] -= cost[pos]
        acc = 0
        mini = float('inf')
        minipos = -1
        for (pos,gaso) in enumerate(gas):
            acc += gaso
            if acc < mini:
                mini = acc
                minipos = (pos + 1) % len(gas)
        return minipos if acc >= 0 else -1
