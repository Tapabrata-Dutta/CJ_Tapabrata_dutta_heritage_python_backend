def subsets(nums, current=[], index=0):

    if index == len(nums):
        print(current)
        return

    subsets(nums, current + [nums[index]], index + 1)

    subsets(nums, current, index + 1)

nums = [1, 2, 3]

subsets(nums)