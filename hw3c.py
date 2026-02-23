#region imports
from math import sqrt
from copy import deepcopy
#endregion


#region helper functions

def separateAugmented(Aaug):
    """
    Separates augmented matrix into A and b.
    """
    A = deepcopy(Aaug)
    b = []
    n = len(A[0]) - 1

    for row in A:
        b.append(row.pop(n))

    return A, b


def BackSolve(A, b, UT=True):
    """
    Solves triangular system Ax=b.
    UT=True  -> Upper triangular
    UT=False -> Lower triangular
    """
    n = len(b)
    x = [0]*n

    if UT:
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(i+1, n):
                s += A[i][j]*x[j]
            x[i] = (b[i] - s)/A[i][i]
    else:
        for i in range(n):
            s = 0
            for j in range(i):
                s += A[i][j]*x[j]
            x[i] = (b[i] - s)/A[i][i]

    return x


def isSymmetric(A):
    """
    Checks if matrix A is symmetric.
    """
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

#endregion


#region Doolittle method

def LUFactorization(A):
    """
    Doolittle LU Factorization.
    """
    n = len(A)
    L = [[0]*n for _ in range(n)]
    U = [[0]*n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1

    for j in range(n):

        for k in range(j, n):
            s = 0
            for s_index in range(j):
                s += L[j][s_index]*U[s_index][k]
            U[j][k] = A[j][k] - s

        for i in range(j+1, n):
            s = 0
            for s_index in range(j):
                s += L[i][s_index]*U[s_index][j]
            L[i][j] = (A[i][j] - s)/U[j][j]

    return L, U


def Doolittle(Aaug):
    """
    Solves Ax=b using Doolittle method.
    """
    A, b = separateAugmented(Aaug)
    L, U = LUFactorization(A)

    y = BackSolve(L, b, UT=False)
    x = BackSolve(U, y, UT=True)

    return x

#endregion


#region Cholesky method

def Cholesky(A):
    """
    Cholesky factorization.
    """
    n = len(A)
    L = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):

            s = 0
            for k in range(j):
                s += L[i][k]*L[j][k]

            if i == j:
                val = A[i][i] - s
                if val <= 0:
                    raise ValueError("Not positive definite")
                L[i][j] = sqrt(val)
            else:
                L[i][j] = (A[i][j] - s)/L[j][j]

    return L


def SolveCholesky(Aaug):
    """
    Solves Ax=b using Cholesky.
    """
    A, b = separateAugmented(Aaug)
    L = Cholesky(A)

    y = BackSolve(L, b, UT=False)

    n = len(L)
    LT = [[L[j][i] for j in range(n)] for i in range(n)]

    x = BackSolve(LT, y, UT=True)

    return x

#endregion


#region main

def main():
    """
    HW3 Part (c)
    Selects Cholesky or Doolittle method automatically.
    """

    print("HW3 – Part (c)")
    print("---------------------------")

    n = int(input("Enter number of rows: "))
    Aaug = []

    for i in range(n):
        row = input("Row {} (comma separated): ".format(i+1))
        row = [float(x) for x in row.split(',')]
        Aaug.append(row)

    A, _ = separateAugmented(Aaug)

    if isSymmetric(A):
        try:
            x = SolveCholesky(Aaug)
            method = "Cholesky Method"
        except:
            x = Doolittle(Aaug)
            method = "Doolittle Method (Not Positive Definite)"
    else:
        x = Doolittle(Aaug)
        method = "Doolittle Method (Not Symmetric)"

    print("Method Used:", method)
    print("Solution:", [round(val,6) for val in x])

#endregion


if __name__ == "__main__":
    main()
