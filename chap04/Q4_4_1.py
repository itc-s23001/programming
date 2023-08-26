vote_num = 0

def vote():
    global vote_num
    vote_num += 1

def reset_box():
    global vote_num
    vote_num = 0

def check_box():
    global vote_num
    print(f"投票箱の中の票数: {vote_num}")

# 投票と箱の確認をテスト
vote()
vote()
vote()
check_box()  # 投票箱の中の票数: 3

reset_box()
check_box()  # 投票箱の中の票数: 0

