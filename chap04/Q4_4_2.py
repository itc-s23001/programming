def create_voting_box():
    vote_num = 0

    def vote():
        nonlocal vote_num
        vote_num += 1

    def reset_box():
        nonlocal vote_num
        vote_num = 0

    def check_box():
        print(f"投票箱の中の票数: {vote_num}")

    return vote, reset_box, check_box

vote_func, reset_func, check_func = create_voting_box()

vote_func()
vote_func()
vote_func()
check_func()  # 投票箱の中の票数: 3

reset_func()
check_func()  # 投票箱の中の票数: 0

