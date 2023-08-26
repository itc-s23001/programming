def join_with_separator(words, separator):
    result = separator.join(words)
    return result

words_list = ['a', 'b', 'c', 'd']
separator = '_'
result = join_with_separator(words_list, separator)
print(result)  # 出力: 'a_b_c_d'

