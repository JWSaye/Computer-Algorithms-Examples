def poly_multiplication_naive(P, Q):
    # P and Q are two polynomials of degree n
    # Runs in O(n^2)
    return [P[i] * Q[j] for i in range(len(P)) for j in range(len(Q))]

def poly_multiplication_Alg1(P, Q):
    # P and Q are two polynomials of degree n
    # Runs in O(n^2)
    n = len(P)
    if n == 1:
        return [P[0] * Q[0]]
    
    else:
        A = P[:n//2]
        B = P[n//2:]
        C = Q[:n//2]
        D = Q[n//2:]
        AC = poly_multiplication_Alg1(A, C)
        BD = poly_multiplication_Alg1(B, D)
        AD = poly_multiplication_Alg1(A, D)
        BC = poly_multiplication_Alg1(B, C)
        ANS = [0] * n
        ANS[0] = AC
        ANS[n/2] = AD + BC
        ANS[n] = BD
        return ANS
        