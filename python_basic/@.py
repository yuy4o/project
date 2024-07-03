# source: https://builtin.com/software-engineering-perspectives/python-symbol


# import numpy as np
# def dot(v1,v2):
#     sum = 0
#     for x, y in zip(v1, v2):
#         sum += x*y
#     return sum

# def value():
#     v1 = np.random.randn(1,4)
#     v2 = np.random.randn(1,4)
#     return v1, v2

# print(value())
# print(dot(value()[0], value()[1]))

# use decorator @

import numpy as np

# @下， value-v 类型是 function 作为 plus的输入，除了 type 不知道还能输出什么
# 因为索引问题，未解决dot, 换用简单的plus
def plus(v):
    print(type(v))


@plus
def value():
    return np.random.randn(1, 4)
