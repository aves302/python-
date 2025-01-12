"""
判断一个数是否是素数。素数是大于1的正整数，且只能被1和它自己整除
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 示例使用
num = 11
print(f"{num} is prime: {is_prime(num)}")
