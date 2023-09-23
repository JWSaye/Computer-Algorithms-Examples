def selection_problem_naive(A, k):
    # Find the kth smallest element in A
    # Runs in O(nlogn)
    A.sort()
    return A[k-1]

def median(A):
    # Find the median of A
    # A will always be small
    A.sort()
    n = len(A)
    if n % 2 == 0:
        return (A[n//2] + A[n//2 - 1]) / 2
    else:
        return A[n//2]

def pivot_Alg1(A, k):
    # Find the kth smallest element in A
    # Runs in O(1)
    n = len(A)
    return median([A[0], A[n//2], A[n-1]])
    
def pivot_Alg2(A, k):
    # Find the kth smallest element in A
    # Runs in O(n)
    n = len(A)
    g = 5
    M = []
    for i in range(n//g):
        M.append(median(A[g*i:g*i+g]))
    return Select(M, (1 + n/g)/2, 2)

def Select(A, k, alg):
    pivot = pivot_Alg1(A, k) if alg == 1 else pivot_Alg2(A, k)