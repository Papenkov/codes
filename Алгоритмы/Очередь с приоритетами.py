'''
Реализация очереди с приоритетами без использования heapq

Первая строка входа содержит число операций 1 ≤ n ≤ 10^5
Каждая из последующих n строк задают операцию одного из следующих двух типов:

- Insert x, где 0 ≤ x ≤ 10^9 — целое число;
- ExtractMax.

Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

Sample:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Answer:
200
500
'''

heap = []
def insert(x):
    heap.append(x)
    i = len(heap) - 1
    while heap[i] > heap[(i-1)//2] and i != 0:
        k = heap[i]
        heap[i] = heap[(i-1)//2]
        heap[(i-1)//2] = k
        i = (i-1)//2

def getMax():
    print(heap[0])
    heap[0] = heap[-1]
    heap.pop(-1)
    i = 0
    try:
        while heap[i] < max(heap[2*i+1], heap[2*(i+1)]):
            k = heap[i]
            if heap[2*i+1] > heap[2*(i+1)]:
                heap[i] = heap[2 * i + 1]
                heap[2 * i + 1] = k
                i = 2*i+1
            else:
                heap[i] = heap[2 * (i + 1)]
                heap[2 * (i + 1)] = k
                i = 2*(i+1)
    except:
        try:
            if heap[i] < heap[2*i+1]:
                k = heap[i]
                heap[i] = heap[2 * i + 1]
                heap[2 * i + 1] = k
        except: return

for _ in range(int(input())):
    inp = input().split()
    if inp[0] == 'Insert':
        insert(int(inp[1]))
    elif inp[0] == 'ExtractMax':
        getMax()