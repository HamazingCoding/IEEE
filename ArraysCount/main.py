def count_distinct_arrays(T, cases):
    for case in cases:
        N, K = case
        max_integers = K + 1
        min_integers = bin((1 << N) - 1).count('1')  # Count the number of ones in binary representation
        result = 0

        for r in range(min_integers, max_integers + 1):
            result += (1 << (r - 1)) % 4

        print(result % 4)

# Read the number of cases
T = int(input())

cases = []
# Read the cases
for _ in range(T):
    N, K = map(int, input().split())
    cases.append((N, K))

# Solve and print the results
count_distinct_arrays(T, cases)