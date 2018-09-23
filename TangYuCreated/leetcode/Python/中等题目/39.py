class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        reference = [
            [] for i in range(target)
        ]
        #reference[i] is the set of all the combinations resulting in target == i + 1
        if 1 in candidates:
            reference[0].append([1])
        for tar in range(1,target):
            for biggest in candidates:
                if biggest == tar + 1:
                    reference[tar].append([biggest])
                elif biggest < tar + 1:
                    for element in reference[tar - biggest]:
                        if element[-1] <= biggest:
                            reference[tar].append(element + [biggest])
        return reference[target - 1]
