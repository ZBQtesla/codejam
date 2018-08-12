class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda person:person[1])
        people.sort(reverse = True,key = lambda person:person[0])
        result = []
        for person in people:
            result.insert(person[1],person)
        return result
