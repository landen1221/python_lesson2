def weekday_name(day_of_week):
    day_name = {1:'Sunday', 2:'Monday', 3:"Tuesday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    if 0 <= day_of_week <=7:
        return day_name[day_of_week]
    return None


print(weekday_name(10))