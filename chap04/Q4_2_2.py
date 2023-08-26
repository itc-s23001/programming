def perrin_sequence(limit=100):
    sequence = [3, 0, 2]
    n = 3
    while True:
        next_term = sequence[n - 2] + sequence[n - 3]
        if next_term >= limit:
            break
        sequence.append(next_term)
        n += 1
    return sequence

result = perrin_sequence(100)
print(result)

