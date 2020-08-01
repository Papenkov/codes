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
    #print(heap, 'после insert')
    try:
        while heap[i] < max(heap[2*i+1], heap[2*(i+1)]) and i < len(heap):
            k = heap[i]
            if heap[2*i+1] > heap[2*(i+1)]:
                heap[i] = heap[2 * i + 1]
                heap[2 * i + 1] = k
                i = 2*i+1
            else:
                heap[i] = heap[2 * (i + 1)]
                heap[2 * (i + 1)] = k
                i = 2*(i+1)
            #print(heap, "сделали один getMax")  вконце неправильно сортирует SwiftDown
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
        #print(heap, 'это наша куча после добавления и сортировки')
    elif inp[0] == 'ExtractMax':
        getMax()
        #print(heap, 'after sort')


# РЕАЛИЗАЦИЯ БЕЗ ФУНКЦИИ
'''heap = []

for _ in range(int(input())):
    inp = input().split()
    if inp[0] == 'Insert':
        heap.append(int(inp[1]))
        i = len(heap) - 1
        while heap[i] > heap[(i - 1) // 2] and i != 0:
            k = heap[i]
            heap[i] = heap[(i - 1) // 2]
            heap[(i - 1) // 2] = k
            i = (i - 1) // 2

    elif inp[0] == 'ExtractMax':
        print(heap[0])
        heap[0] = heap[-1]
        heap.pop(-1)
        i = 0
        try:
            while heap[i] < max(heap[2 * i + 1], heap[2 * (i + 1)]) and i < len(heap):
                k = heap[i]
                m = heap.index(max(heap[2 * i + 1], heap[2 * (i + 1)]))
                heap[i] = heap[m]
                heap[m] = k
                i = m
        except:
            pass'''