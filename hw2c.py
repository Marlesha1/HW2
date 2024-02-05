import numpy as np


def is_diagonally_dominant(matrix):
    diagonal = np.abs(matrix.diagonal())
    row_sums = np.sum(np.abs(matrix), axis=1) - diagonal
    return np.all(diagonal >= row_sums)
'''this is checking to see if it is diagonaly dominant in the matrix'''


def GaussSeidel(Aaug, x, Niter=15):
    A = Aaug[:, :-1]
    b = Aaug[:, -1]

    if not is_diagonally_dominant(A):
        raise ValueError("Matrix is not diagonally dominant.")

    n = len(b)
    x = x.copy()

    for _ in range(Niter):
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]

    return x


def main():
    # Example 1
    A1 = np.array([[4, -1, 0, 3],
                   [1, 15.5, 3, 8],
                   [0, -1.3, -4, 1.1],
                   [14, 5, -2, 30]])
    b1 = np.array([1, 1, 1, 1])
    x1_initial_guess = np.zeros_like(b1)

    print("Solution for Example 1:")
    result1 = GaussSeidel(np.column_stack((A1, b1)), x1_initial_guess)
    print(result1)

    # Example 2
    A2 = np.array([[4, -1, 0, 3],
                   [1, 15.5, 3, 8],
                   [0, -1.3, -4, 1.1],
                   [14, 5, -2, 30]])
    b2 = np.array([1, 1, 1, 1])
    x2_initial_guess = np.zeros_like(b2)

    print("\nSolution for Example 2:")
    result2 = GaussSeidel(np.column_stack((A2, b2)), x2_initial_guess)
    print(result2)


if __name__ == "__main__":
    main()
