def solution(nums):
    new_nums = set(nums)

    return len(nums) // 2 if len(new_nums) >= len(nums) // 2 else len(new_nums)