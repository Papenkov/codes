'''

Вычислить расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита.

Sample Input:
short
ports

Output:
3

'''

A = input()
B = input()

def diff(x, y):
    if x == y:
        return 0
    else:
        return 1

D = [[int(i) for i in range(len(B) + 1)]]
for i in range(1, len(A) + 1):
    D.append([i])
    for j in range(1, len(B) + 1):
        res = min(D[i][j - 1] + 1, D[i - 1][j] + 1, D[i - 1][j - 1] + diff(A[i - 1], B[j - 1]))
        D[i] += [res]
print(res)