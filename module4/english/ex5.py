correct_account = "python"
correct_password = "ruLeS"

guesses = 0

while guesses < 5:
    username = input("Account: ")
    password = input("Password: ")

    if username == correct_account and password == correct_password:
        print("Welcome")
        break

    guesses = guesses + 1

else:
    print("Access denied")
