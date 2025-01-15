"""
查找列表中的重复元素
"""
def find_duplicates(lst):
    seen = set()
    duplicates = set(x for x in lst if x in seen or seen.add(x))
    return duplicates

# 示例使用
my_list = [1, 2, 3, 4, 2, 5, 6, 3]
print(f"Duplicate elements: {find_duplicates(my_list)}")
