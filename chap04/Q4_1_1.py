def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

number = int(input("フィボナッチ数列を計算する上限値を入力してください: "))
fibonacci_sequence(number)

