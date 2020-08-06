'''
В первой строке дан массив "lst" из натуральных чисел в порядке возрастания,
во второй — натуральные числа (k).
Найти индекс каждого числа k в массиве lst, если k нет в lst - вывести "-1".

Input:
1 5 8 12 13    # lst
8 1 23 1 11

Output:
3 1 -1 1 -1
'''

lst = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
for i in lst2:
    l, r = 0, len(lst)
    while l <= (r-1):
        mid = (l + r)//2
        if lst[mid] == i:
            print(mid+1, end=' ')
            break
        elif lst[mid] < i:
            l = mid + 1
        elif lst[mid] > i:
            r = mid
        if l > r - 1:
            print(-1, end=' ')