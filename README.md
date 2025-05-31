
🔐 PassForge - Custom Password Generator Tool

PassForge is a Python-based interactive tool that generates strong, personalized passwords based on optional user input. It also evaluates and saves the generated passwords with strength levels.


---

📦 Requirements

Make sure you have Python 3 installed. No external packages are required — only built-in Python libraries are used.


---

⚙️ Installation

1. Clone or download the tool:



git clone https://github.com/your-username/passforge.git
cd passforge

2. (Optional) Create a virtual environment:



python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Run the tool directly:



python3 passforge.py --interactive


---

🚀 Usage Instructions

To launch PassForge in interactive mode:

python3 passforge.py --interactive

You’ll be prompted to enter:

First name (optional)

Last name (optional)

Hobby (optional)

Year of birth (optional)

Country (optional)

Password length (default: 12)

Number of password attempts to generate (default: 1)


The generated passwords will be printed and saved in a file called passwords.txt.


---

📊 Example Output

========================================

Password 1: John@492913
Strength: Very Strong


---

💡 Features

Personalized password patterns

Automatic strength scoring (Weak → Excellent)

Password length customization

Multiple output formats

Saves passwords to passwords.txt



---

📁 File Structure

passforge.py          # Main tool script
passwords.txt         # Output file (auto-created)


---

✅ License

Open-source. You can modify and use PassForge freely under the MIT license (or your choice).
