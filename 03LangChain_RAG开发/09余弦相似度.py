import numpy as np

def get_dot(a, b):
    """计算2个向量的点积，2个向量同维度数字乘积之和"""
    dot_sum = 0
    if len(a) != len(b):
        raise ValueError("两个向量必须维度相同")
    for a, b in zip(a, b):
        dot_sum += a * b
    return dot_sum

def get_norm(x):
    """计算单个向量的模长"""
    sum_square = 0
    for v in x:
        sum_square += v ** 2
    return np.sqrt(sum_square)

# a = (1, 2, 3)
# b = (2, 3, 4)
# for a, b in zip(a, b):
#     print(a, b)

def cosine_similarity(a, b):
    """计算余弦相似度"""
    print(get_dot(a, b) / (get_norm(a) * get_norm(b)))


if __name__ == '__main__':
    a = (1, 2, 3)
    b = (2, 3, 4)
    c = (2, 4, 6)
    cosine_similarity(a, b)
    cosine_similarity(a, c)
