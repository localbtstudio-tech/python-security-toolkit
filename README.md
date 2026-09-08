# 🔐 Python Security Toolkit

A beginner-friendly **Python security toolkit** that combines essential security utilities into a simple command-line application.

This project was built as a practical exercise to strengthen my **Python programming fundamentals** while exploring basic cybersecurity concepts such as **password generation, password strength analysis, and cryptographic hashing**.

---

## 📸 Project Preview

```text
-------------------------------------
|      PYTHON SECURITY TOOLKIT      |
|              V1.1                 |
-------------------------------------

1. Password Generator
2. Password Strength Checker
3. Hash Generator
4. Exit
```

---

## ✨ Features

### 🔑 Password Generator

Generate secure random passwords using Python's `secrets` module.

* Random uppercase and lowercase letters
* Numbers
* Special characters
* Configurable password length
* Length range: **4–128 characters**
* Uses cryptographically secure randomness

### 🛡️ Password Strength Checker

Analyze a password based on several basic security criteria.

The checker evaluates:

* Password length
* Lowercase characters
* Uppercase characters
* Numbers
* Special characters

The password is classified as:

* 🔴 **Weak**
* 🟡 **Medium**
* 🟢 **Strong**

### #️⃣ Hash Generator

Convert text into a **SHA-256 hash** using Python's built-in `hashlib` library.

Example:

```text
Input:
Hello World

SHA-256:
a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b...
```

---

## 🧠 What I Learned

This project helped me practice several important Python concepts:

* Variables and data types
* `if / elif / else`
* `for` loops
* Functions
* `try / except`
* User input
* String manipulation
* Boolean variables
* Python modules
* Working with `secrets`
* Working with `string`
* Cryptographic hashing with `hashlib`
* Building a menu-driven CLI application
* Structuring a Python project into reusable functions

---

## 🛠️ Technologies

| Technology    | Purpose                           |
| ------------- | --------------------------------- |
| 🐍 Python     | Main programming language         |
| 🔐 `secrets`  | Secure random password generation |
| 🔤 `string`   | Character sets                    |
| #️⃣ `hashlib` | SHA-256 hashing                   |
| 💻 CLI        | User interaction                  |

---

## ⚙️ How It Works

```text
                ┌─────────────────────┐
                │        START        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Display Menu     │
                └──────────┬──────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │  Password  │ │  Password  │ │    Hash    │
      │ Generator  │ │   Checker  │ │ Generator  │
      └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
            │              │              │
            ▼              ▼              ▼
       Generate       Analyze        SHA-256
       Password       Strength         Hash
            │              │              │
            └──────────────┼──────────────┘
                           ▼
                ┌─────────────────────┐
                │    Return to Menu   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │        EXIT         │
                └─────────────────────┘
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/localbtstudio-tech/python-security-toolkit.git
```

### 2. Navigate to the project

```bash
cd python-security-toolkit
```

### 3. Run the program

```bash
python main.py
```

---

## 📁 Project Structure

```text
python-security-toolkit/
│
├── main.py
└── README.md
```

---

## 🔒 Security Note

This project is **educational** and demonstrates basic security concepts.

The password strength checker uses a simple rule-based scoring system and should **not** be considered a complete password security auditing solution.

Also, **SHA-256 is a general-purpose cryptographic hash**, not a password-storage algorithm. Real applications should use dedicated password-hashing algorithms such as **Argon2, bcrypt, or scrypt** with appropriate parameters.

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Stronger password strength analysis
* [ ] Password entropy calculation
* [ ] Configurable character sets
* [ ] Multiple hashing algorithms
* [ ] File hashing
* [ ] Hash verification
* [ ] Colored CLI interface
* [ ] Password generation options
* [ ] Unit tests
* [ ] Better project structure
* [ ] Logging and error handling improvements

---

## 📌 Version

**Current Version:** `V1.1`

---

## 👨‍💻 Author

**Hamza Weslati**

IT Student · Web Developer · Software Development

🔗 GitHub: `localbtstudio-tech`

---

### 💡 Learn. Build. Secure. Repeat.

> A small project built to strengthen Python fundamentals and explore cybersecurity concepts through practice.
