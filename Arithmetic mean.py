def ArithmeticSequences(A, B):

    if (B <= 2):
        return 0

    count = 0

    res = 0

    for i in range(2, B):

        if ((A[i] - A[i - 1]) == (A[i - 1] - A[i - 2])):
            count += 1

        else:
            count = 0
        res += count

    return res

A = [1, 3, 5, 6, 7, 8]
B = len(A)

print(ArithmeticSequences(A, B))
