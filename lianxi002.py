"""
将一个字符串中的每个单词反转
"""
def reverse_words(s):
    # 按照空格将字符串拆分成单词列表
    words = s.split()
    
    # 对每个单词进行反转
    reversed_words = [word[::-1] for word in words]
    
    # 将反转后的单词合并成一个新的字符串，单词之间用空格分隔
    return ' '.join(reversed_words)

# 示例使用
s = "Hello World"
result = reverse_words(s)
print(f"反转后的字符串: {result}")
