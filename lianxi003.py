"""
题目：反转字符串中的单词
题目要求：

给定一个字符串 s，你需要反转字符串中的单词顺序。
保留单词中的空格，但是每个单词的位置需要反转。
"""
def reverse_words(s):
    # 将字符串按空格分割成单词
    words = s.split()
    
    # 反转单词列表
    reversed_words = words[::-1]
    
    # 将反转后的单词列表重新合并为一个字符串
    return ' '.join(reversed_words)

# 示例使用
s = "The quick brown fox"
result = reverse_words(s)
print(result)
