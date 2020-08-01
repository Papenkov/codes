'''
Задача на число инверсий.

Первая строка содержит число 1 ≤ n ≤ 10^5,
вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1 ≤ i < j ≤ n, для которых A[i] > A[j]. (Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например,
в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию,
инверсию образуют каждые два элемента.)

Input:
5
2 3 9 2 9

Output:
2
'''


n = int(input())
lst = list(map(int, input().split()))

def Merge(a, b):
    global cnt
    new_lst = []
    while a and b:
        if a[0] <= b[0]:
            new_lst += [a.pop(0)]
        else:
            new_lst += [b.pop(0)]
            cnt += (len(a))
    if not a:
        new_lst += b
    elif not b:
        new_lst += a
    return new_lst

def Sort(a):
    if len(a) == 1: return a
    m = len(a)//2
    left = a[0: m]
    right = a[m:]
    left = Sort(left)
    right = Sort(right)
    return Merge(left, right)

cnt = 0
Sort(lst)
print(cnt)