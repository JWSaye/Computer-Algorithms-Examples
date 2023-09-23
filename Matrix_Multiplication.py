def matrix_multiplication_naive(A, B):
    # A and B are two matrices of size n x n
    # Runs in O(n^3)
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_multiplication_Alg1(A, B):
    # A and B are two matrices of size n x n
    # Runs in O(n^3)
    n = len(A)
        
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    if n//2 == 1:
        # Add extra column and row of zeros to make n even
        A = [A, [0] * n]
        A = [row + [0] for row in A]
    
    S = [row[:n//2] for row in A[:n//2]]
    T = [row[n//2:] for row in A[:n//2]]
    U = [row[:n//2] for row in A[n//2:]]
    V = [row[n//2:] for row in A[n//2:]]
    W = [row[:n//2] for row in B[:n//2]]
    X = [row[n//2:] for row in B[:n//2]]
    Y = [row[:n//2] for row in B[n//2:]]
    Z = [row[n//2:] for row in B[n//2:]]
    C11 = matrix_multiplication_Alg1(S, W) + matrix_multiplication_Alg1(T, Y)
    C12 = matrix_multiplication_Alg1(S, X) + matrix_multiplication_Alg1(T, Z)
    C21 = matrix_multiplication_Alg1(U, W) + matrix_multiplication_Alg1(V, Y)
    C22 = matrix_multiplication_Alg1(U, X) + matrix_multiplication_Alg1(V, Z)
    return [[C11, C12], [C21, C22]]

def matrix_multiplication_Strassen(A, B):
    # A and B are two matrices of size n x n
    # Runs in O(n^2.81)
    n = len(A)
        
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    if n//2 == 1:
        # Add extra column and row of zeros to make n even
        A = [A, [0] * n]
        A = [row + [0] for row in A]
    
    S = [row[:n//2] for row in A[:n//2]]
    T = [row[n//2:] for row in A[:n//2]]
    U = [row[:n//2] for row in A[n//2:]]
    V = [row[n//2:] for row in A[n//2:]]
    W = [row[:n//2] for row in B[:n//2]]
    X = [row[n//2:] for row in B[:n//2]]
    Y = [row[:n//2] for row in B[n//2:]]
    Z = [row[n//2:] for row in B[n//2:]]
    
    P1 = matrix_multiplication_Strassen(S, X - Z)
    P2 = matrix_multiplication_Strassen(S + T, Z)
    P3 = matrix_multiplication_Strassen(U + V, W)
    P4 = matrix_multiplication_Strassen(V, Y - W)
    P5 = matrix_multiplication_Strassen(S + V, W + Z)
    P6 = matrix_multiplication_Strassen(T - V, Y + Z)
    P7 = matrix_multiplication_Strassen(S - U, W + X)
    
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P1 + P5 - P3 - P7
    
    return [[C11, C12], [C21, C22]]