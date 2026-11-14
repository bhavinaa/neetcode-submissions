# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        length = len(pairs)
        result =[]

        for i in range(0, length):
            value = pairs[i]
            j = i - 1
            while j >= 0:
                if (value.key < pairs[j].key):
                    pairs[j + 1], pairs[j] = pairs[j], pairs[j + 1]
                    value = pairs[j]
                j = j  - 1
            result.append(pairs[:])
        return result

        