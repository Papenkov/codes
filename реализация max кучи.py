
# Реализация max кучи с имеющимся массивом

import random
B = []

for n in range(15):
    B.append(random.randint(1, 200))    #цикл для генерации случайного массива

print(B)
n = len(B)
p = (n // 2) - 1

def SiftDown(A, p):
    if 2 * (p + 1) < n:
        s1 = (2 * p) + 1
        s2 = 2 * (p + 1)
        if A[p] < A[s1] or A[p] < A[s2]:
            if A[s1] >= A[s2]:
                A[p], A[s1] = A[s1], A[p]
                if s1 <= (n // 2) - 1:
                    SiftDown(A, s1)
            else:
                A[p], A[s2] = A[s2], A[p]
                if s2 <= (n // 2) - 1:
                    SiftDown(A, s2)
    else:
        s = (2 * p) + 1
        if A[p] < A[s]:
            A[p], A[s] = A[s], A[p]
            if s <= (n // 2) - 1:
                SiftDown(A, s)


for i in range(p, -1, -1):
    SiftDown(B, i)
print(B)
