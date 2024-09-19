# tuple data structure
# position       1        2        3       4
# index          0        1        2       3
seasons = ("winter", "spring", "summer", "autumn")

def get_season(month_number):
    if month_number in [12, 1, 2]:
        return seasons[0]
    elif month_number in [3, 4, 5]:
        return seasons[1]
    elif month_number in [6, 7, 8]:
        return seasons[2]
    elif month_number in [9, 10, 11]:
        return seasons[3]
    else:
        return "?????"

#    position       1        2         3         4         5         6         7         8         9        10        11        12
#    index          0        1         2         3         4         5         6         7         8         9        10        11
long_seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")

def get_season2(month_number):
    if month_number > 12:
        return "?????"
    return long_seasons[month_number - 1]

def get_value():
    return input("Enter month number (empty to quit): ")

month_str = get_value()
while month_str != "":
    print(get_season(int(month_str)))
    print(get_season2(int(month_str)))

    month_str = get_value()