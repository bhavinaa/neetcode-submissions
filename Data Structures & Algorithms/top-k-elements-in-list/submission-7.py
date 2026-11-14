class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # calculate the frequency
        total = {}
        for i in range(0, len(nums)):
            v = nums[i]
            if v in total:
                total[v] = total[v] + 1
            else:
                total[v] = 1
        # sort by the ascending frequency
        # (value, freq)
        temp = sorted(total.items(), key = lambda item: item[1], reverse=True)
        t2 = list(map(lambda x: x[0], temp))
   
        # print(temp.items())
        # return as much as you can, as you wont get one at every count
        result = []
      
        for i in range(0,k):
            t1 = t2[i]
            result.append(t1)
        return result