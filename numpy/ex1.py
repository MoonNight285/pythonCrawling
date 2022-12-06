import numpy as np

print(np.__version__)

ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)
print(type(ar1))

# ar2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
# print(ar2)

# 1 ~ 11 까지 증가값이 2
ar3 = np.arange(1, 11, 2)
print(ar3)

ar4 = np.arange(1, 31, 3)
print(ar4)

ar5 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
print(ar5)

ar6 = np.zeros((2, 3))
print(ar6)

ar7 = np.array([[10, 20, 30], [40, 50, 60]])
ar8 = ar7[0:2, 0:2]
print(ar8)

ar9 = ar7[0:]
print(ar9)

print("-----------")
ar10 = ar7[0, :]
print(ar10)

ar11 = np.array([1, 2, 3, 4, 5])
ar12 = ar11 + 10

ar13 = ar11 + ar12

ar14 = ar13 * 2
print(ar14)