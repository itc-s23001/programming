numbers = range(1, 8)
padded_strings = map(lambda x: f"{x:04}", numbers)
padded_strings_list = list(padded_strings)

print(padded_strings_list)

