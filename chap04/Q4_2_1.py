from datetime import datetime, timedelta

def classify_date(days_offset=0):
    today = datetime.now().date()
    target_date = today + timedelta(days=days_offset)
    
    diff = (target_date - today).days
    if diff == -1:
        return "昨日"
    elif diff == 0:
        return "今日"
    elif diff == 1:
        return "明日"
    else:
        return "今日より1日を超えて離れた日"

print(classify_date())
print(classify_date(-1))
print(classify_date(1))
print(classify_date(2))

