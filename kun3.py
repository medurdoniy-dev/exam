

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    sorted_nums = sorted(nums, key=lambda x: (-freq[x], x))
    return sorted_nums

#  test:
print(rearrange_by_frequency([]))
