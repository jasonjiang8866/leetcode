class Solution(object):
    def twoSum(self, nums:list, target:int)-> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable={}
        for index, item in enumerate(nums):
            compliment=target-item
            if hashTable.get(compliment, None) is not None:
                return [hashTable[compliment], index]
            else:
                hashTable[item]=index
