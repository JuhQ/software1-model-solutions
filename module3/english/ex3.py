gender = input("Provide gender: ")
hemoglobin = int(input("Provide hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Low")
    elif 117 <= hemoglobin <= 175:
        print("Normal")
    else:
        print("High")

elif gender == "male":
    if hemoglobin < 134:
        print("Low")
    elif 134 <= hemoglobin <= 195:
        print("Normal")
    else:
        print("High")
else:
    print("Gender should be written lowercase. Options: female, male.")