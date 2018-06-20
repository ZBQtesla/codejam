class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        reference = {}
        for char in ransomNote:
            if char in reference:
                reference[char] += 1
            else:
                reference[char] = 1
        for char in reference:
            if magazine.count(char) < reference[char]:
                return False
        return True
