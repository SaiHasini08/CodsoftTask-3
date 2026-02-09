while True:
    print("\n--- PASSWORD GENERATOR ---")
    print("1. Letters only")
    print("2. Letters and Numbers")
    print("3. Letters, Numbers and Symbols")

    choice = input("Choose password type (1/2/3): ")
    length = int(input("Enter password length: "))

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    if choice == "1":
        chars = letters
    elif choice == "2":
        chars = letters + numbers
    elif choice == "3":
        chars = letters + numbers + symbols
    else:
        print("Invalid choice")
        continue

    password = ""
    index = 1

    while len(password) < length:
        password = password + chars[index % len(chars)]
        index = index + 3

    print("Generated Password:", password)

    again = input("Do you want to generate another password? (yes/no): ")
    if again != "yes":
        print("Program closed.")
        break
