from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i_idx, j_idx = 0, len(numbers) - 1

        lowest = min(numbers)

        if lowest < 0:
            target = target - 2*lowest
            numbers = [number - lowest for number in numbers]

        while i_idx < j_idx and j_idx > 0:
            i = numbers[i_idx]
            j = numbers[j_idx]
            val = i + j
            # print(i_idx, ":", i)
            # print(j_idx, ":", j)
            # print(val)
            if val == target and i_idx != j_idx :
                print(i,j)
                break
            else:
                if val > target:
                    j_idx -= 1
                else:
                    i_idx += 1

        return [i_idx+1, j_idx+1]




# print(Solution().twoSum(
#     numbers = [2,3,4], target = 6
# ))