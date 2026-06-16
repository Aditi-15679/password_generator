import string
import secrets
import math

print("\nWelcome to Secure Password Generator")
print("-" * 40)

while True:

    # Taking password length from user
    while True:
        try:
            password_length = int(input("Enter password length (15-64): "))

            if 15 <= password_length <= 64:
                break
            else:
                print("Password length should be between 15 and 64.")

        except ValueError:
            print("Please enter a valid number.")

    # Creating character pool
    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Generating password
    password_characters = []

    for i in range(password_length):
        random_character = secrets.choice(all_characters)
        password_characters.append(random_character)

    generated_password = "".join(password_characters)

    # Entropy calculation
    pool_size = len(all_characters)
    entropy = password_length * math.log2(pool_size)

    # Password strength analysis
    if entropy < 60:
        strength = "Weak"
    elif entropy < 100:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Length-based recommendation
    if 15 <= password_length <= 20:
        recommendation = "Good Security"
    elif 21 <= password_length <= 32:
        recommendation = "High Security"
    else:
        recommendation = "Excellent Security"

    # Output
    print("\n" + "=" * 50)
    print("GENERATED PASSWORD")
    print("=" * 50)
    print(generated_password)

    print("\nPassword Report")
    print("-" * 25)
    print("Password Length :", password_length)
    print("Character Pool  :", pool_size)
    print("Entropy         :", round(entropy, 2), "bits")
    print("Strength        :", strength)
    print("Recommendation  :", recommendation)

    # Generate another password option
    choice = input("\nGenerate another password? (Y/N): ").strip().lower()

    if choice != "y":
        print("\nThank you for using Secure Password Generator!")
        break