from typing import List

# NOTACK_COLOR
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1

        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1  # 每次的low 都是指向0之后的位置,不会覆盖当前最小值0
                i += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                # nums[i] == 1
                i += 1
        print(nums)


Solution().sortColors([0, 1, 2, 1, 0, 2,0])
"""
实现思路:
    因为要对0,1,2 进行排序,此处借助快速排序的思路,利用low和high对两头进行操作
    low 始终指向最小数下一个数,high 始终指向最大数前一个数
"""