Enterprise Random Password Generator

Project Overview

The Enterprise Random Password Generator is a Python-based application designed to generate highly secure and unpredictable passwords. The project follows the Input-Process-Output (IPO) architecture and implements modern password generation practices using Python's built-in modules.

The application allows users to specify the desired password length and generates a random password containing uppercase letters, lowercase letters, numbers, and special characters. It also calculates password entropy to estimate the strength and security of the generated password.

---

Objectives

- Generate secure random passwords.
- Validate user input according to recommended password length guidelines.
- Use cryptographically secure randomness.
- Calculate password entropy.
- Provide password strength analysis.
- Demonstrate efficient string handling techniques in Python.

---

Features

- User-defined password length.
- Input validation (15–64 characters).
- Uses uppercase and lowercase letters.
- Uses numeric digits.
- Uses special symbols.
- Cryptographically secure password generation using the "secrets" module.
- Entropy calculation for security analysis.
- Password strength classification.
- Option to generate multiple passwords without restarting the program.

---

Technologies Used

Python Modules

string

Used to access predefined character sets:

- "ascii_letters"
- "digits"
- "punctuation"

secrets

Used for secure random character selection. Unlike the "random" module, "secrets" is designed for security-sensitive applications.

math

Used for entropy calculation through logarithmic functions.

---

Project Architecture

Input

- Password length entered by the user.

Process

1. Validate input.
2. Create character pool.
3. Select random characters securely.
4. Build password using list accumulation.
5. Calculate entropy.
6. Analyze password strength.

Output

- Generated password.
- Password statistics.
- Entropy value.
- Security recommendation.

---

Algorithm

1. Start the program.
2. Ask the user to enter the desired password length.
3. Check whether the length is between 15 and 64.
4. Create a character pool using letters, digits, and symbols.
5. Randomly select characters using "secrets.choice()".
6. Store selected characters in a list.
7. Combine all characters into a password using """.join()".
8. Calculate password entropy.
9. Display the generated password and security details.
10. Ask the user whether another password should be generated.
11. End the program.

---

Password Entropy

Entropy measures how difficult a password is to guess or crack.

Formula:

Entropy = Password Length × log₂(Character Pool Size)

A higher entropy value indicates a stronger and more secure password.

---

Sample Output

Welcome to Secure Password Generator

Enter password length (15-64): 20

Generated Password:
A@7kLm#2Pq!9Rs$XwZ4T

Password Report
-------------------------
Password Length : 20
Character Pool  : 94
Entropy         : 131.09 bits
Strength        : Very Strong
Recommendation  : High Security

---

How to Run

1. Install Python 3.x.
2. Download the project files.
3. Open a terminal in the project folder.
4. Run:

python password_generator.py

5. Enter a password length between 15 and 64.
6. View the generated password and security analysis.

---

Future Improvements

- Graphical User Interface (GUI).
- Password copy-to-clipboard feature.
- Password export functionality.
- Custom character set selection.
- Password history management.

---

Conclusion

The Enterprise Random Password Generator successfully generates secure passwords using modern security practices. By combining cryptographically secure randomness, entropy analysis, and efficient memory management, the project demonstrates practical applications of Python programming in cybersecurity and password management.