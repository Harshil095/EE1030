import cmath
import random

def transpose(A):
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    return [[A[i][j] for i in range(rows)] for j in range(cols)]

def conjugate_transpose(A):
    return [[complex(A[i][j]).conjugate() for i in range(len(A))] for j in range(len(A[0]))]
    
def norm(v):
    return cmath.sqrt(sum(abs(x)**2 for x in v))

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Invalid operation")
    C = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))
    return C

def scalar_mult(v, scalar):
    return [scalar * x for x in v]

def vector_sub(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def identity_matrix(size):
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]

def outer_product(v1, v2):
    return [[x * y.conjugate() for y in v2] for x in v1]

def householder_qr(A):
    m, n = len(A), len(A[0])
    Q = identity_matrix(m)
    R = [row[:] for row in A]

    for i in range(min(m, n)):
        x = [R[j][i] for j in range(i, m)]
        norm_x = norm(x)
        sign = -1 if x[0].real < 0 else 1
        e1 = [1.0] + [0.0] * (len(x) - 1)
        v = vector_sub(x, scalar_mult(e1, sign * norm_x))
        v_norm = norm(v)
        v = scalar_mult(v, 1 / v_norm) if v_norm != 0 else v
        H_partial = outer_product(v, v)
        H = identity_matrix(m)
        for x in range(len(v)):
            for y in range(len(v)):
                H[x + i][y + i] -= 2 * H_partial[x][y]
        R = matrix_multiply(H, R)
        Q = matrix_multiply(Q, H)

    return Q, R
    
def power_iteration(A, max_iterations=1000, tol=1e-9):
    m = len(A)
    n = len(A[0])

    # Ensure the matrix is square
    if m != n:
        raise ValueError("Matrix must be square for power iteration.")

    a_k = [random.random() for _ in range(m)]

    for _ in range(max_iterations):
        a_k1 = [sum(A[i][j] * a_k[j] for j in range(m)) for i in range(m)]
        norm_a_k1 = norm(a_k1)
        a_k1 = [x / norm_a_k1 for x in a_k1]

        if all(abs(a_k1[i] - a_k[i]) < tol for i in range(m)):
            break

        a_k = a_k1

    eigenvalue = sum(
        a_k1[i] * sum(A[i][j] * a_k1[j] for j in range(m)) for i in range(m)
    )

    return eigenvalue
    
def qr_algorithm(A, max_iterations=100, tol=1e-9):
    n = len(A)
    Ak = [row[:] for row in A]
    for _ in range(max_iterations):
        Q, R = householder_qr(Ak)
        Ak = matrix_multiply(R, Q)  # Update 
        off_diagonal_sum = sum(abs(Ak[i][j]) for i in range(n) for j in range(n) if i != j)
        if off_diagonal_sum < tol:
            break

    
    eigenvalues = [Ak[i][i] for i in range(n)]
    return eigenvalues

def method_choice(A):
    print("Choose a method for calculation:")
    print("1. QR Algorithm")
    print("2. Power Iteration")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        eigenvalues = qr_algorithm(A)
        print("Eigenvalues using QR algorithm:", eigenvalues)
    elif choice == '2':
        eigenvalue = power_iteration(A)
        print("Eigenvalue using Power Iteration:", eigenvalue)
    else:
        print("Invalid choice")

# Test matrix
A = [[2, 1, 3], [1, 3, 1], [3, 1, 3]]


method_choice(A)


