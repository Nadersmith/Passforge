🔐 Custom Password Generator with Strength Evaluation

An interactive Python tool to generate strong, customized passwords based on user input, with automatic strength evaluation and password saving.


---

✅ Features

Generates strong, random passwords with custom length and format.

Interactive prompts for user details (name, hobby, birth year, etc.).

Automatic strength evaluation for each password.

Saves generated passwords to passwords.txt.

CLI support using argparse.



---

🧰 Requirements

Python 3.6 or higher



---

📦 Installation

1. Make sure Python is installed
Check Python version:

python --version

or:

python3 --version


2. Download the script

Either copy password_generator.py manually

Or clone the repository:

git clone https://github.com/username/password-generator.git
cd password-generator





---

⚙️ How to Run

Run the tool in interactive mode:

python password_generator.py --interactive

Or, depending on your system:

python3 password_generator.py --interactive

You’ll be prompted for optional inputs like name, hobby, birth year, password length, and number of attempts.


---

📝 Example Output

python3 password_generator.py --interactive

Expected Output:

First name (Press Enter to skip): Peter
Last name (Press Enter to skip): Smith
What is your hobby? (Press Enter to skip): gaming
What is your birth year? (Press Enter to skip): 2000
What is your country? (Press Enter to skip): Jordan
Password length? (Press Enter to skip, default is 12): 16
Number of attempts? (Press Enter to skip, default is 1): 3
========================================
Password 1: Peter@493922
Strength: Strong
Password saved to file.
...


---

📁 Output File

All generated passwords are saved to a file named passwords.txt in the same directory as the script.


---

⚠️ Security Notice

> This tool is intended for educational use. Do not use generated passwords for sensitive or critical accounts without additional review or secure generation methods.




---

✨ Future Improvements (Suggestions)

Add support for enterprise password policies (Google, Microsoft, etc.).

Build a GUI version.

Add full CLI support (non-interactive mode with all options as flags).
