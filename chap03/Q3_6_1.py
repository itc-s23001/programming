import random

target_number = ''.join(random.sample('0123456789', 4))

print("4桁の数字の入力を求めます。")

while True:
    user_input = input("4桁の数字を入力してください（重複なし）: ")

    if not user_input.isdigit() or len(user_input) != 4 or len(set(user_input)) != 4:
        print("無効な入力です。4桁の数字を入力してください。")
        continue

    if user_input == target_number:
        print("正解です！プログラムを終了します。")
        break
    else:
        print("一致しません。もう一度試してみてください。")

