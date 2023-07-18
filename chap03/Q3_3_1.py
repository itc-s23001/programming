my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]


filtered_list = []


for item in my_list:
    if len(item) >= 6:
        filtered_list.append(item)


print(filtered_list)
