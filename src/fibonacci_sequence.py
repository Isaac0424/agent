def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 1, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# 첫 번째 항이 1인 피보나치 수열의 처음 10개 항 출력
print(fibonacci_sequence(10))