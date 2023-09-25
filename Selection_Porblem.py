def selection_problem_naive(Array, k):
    # Find the kth smallest element in Array
    # Runs in O(nlogn)
    Array.sort()
    return Array[k-1]

def median(Array):
    # Find the median of Array
    # Array will always be small
    Array.sort()
    n = len(Array)
    if n % 2 == 0:
        return (Array[n//2] + Array[n//2 - 1]) / 2
    else:
        return Array[n//2]

def pivot_Alg1(Array):
    # Find the pivot of Array
    # Runs in O(1)
    n = len(Array)
    return median([Array[0], Array[n//2], Array[n-1]])
    
def pivot_Alg2(Array):
    # Find the pivot of Array
    # Runs in O(n)
    GROUP_SIZE = 5
    if len(Array) <= GROUP_SIZE:
        return median(Array)
    n = len(Array)
    Medians = []
    for i in range(n//GROUP_SIZE):
        Medians.append(median(Array[GROUP_SIZE*i:GROUP_SIZE*i+GROUP_SIZE]))
    return Select(Medians, (1 + n//GROUP_SIZE)/2, 2)

def Select(Array, k, alg):
    pivot = pivot_Alg1(Array, k) if alg == 1 else pivot_Alg2(Array, k)
    Less, Equal, Greater = [], [], []
    for element in Array:
        if element < pivot:
            Less.append(element)
        elif element == pivot:
            Equal.append(element)
        else:
            Greater.append(element)