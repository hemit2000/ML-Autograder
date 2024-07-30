def div_list(nums1, nums2):
    result = map(lambda x, y: x / y, nums1, nums2)
    return list(result)

print(div_list([10, 20, 30], [3, 5, 9]))
