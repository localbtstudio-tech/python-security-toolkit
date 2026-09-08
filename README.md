# PYTHON SECURITY TOOLKIT 🔐

<div align="center">

### A lightweight command-line security toolkit built with Python.

**Python · Security Fundamentals · Functions · CLI**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Security-black?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

</div>

---

## ◼︎ The Project

A simple but structured **command-line security toolkit** built from scratch with Python.

The project combines several basic security utilities into one application while practicing **functions, loops, conditions, input handling, error handling, modules, password security, and cryptographic hashing**.

> **Small project. Real security fundamentals.**

---

## ✦ What It Can Do

```text
┌─────────────────────────────────────┐
│       PYTHON SECURITY TOOLKIT       │
├─────────────────────────────────────┤
│  1. Password Generator              │
│  2. Password Strength Checker       │
│  3. Hash Generator                  │
│  4. Exit                            │
└─────────────────────────────────────┘
```

### 🔑 Password Generator

* 🔐 Secure random password generation
* 🔤 Uppercase & lowercase characters
* 🔢 Numbers
* 🔣 Special characters
* 📏 Custom length from 4–128 characters
* 🛡️ Uses Python's `secrets` module

### 🛡️ Password Strength Checker

* 📏 Checks password length
* 🔡 Detects lowercase characters
* 🔠 Detects uppercase characters
* 🔢 Detects numbers
* 🔣 Detects special characters
* 📊 Returns Weak, Medium, or Strong

### #️⃣ Hash Generator

* 🔐 Generates a `SHA-256` hash
* ⚡ Uses Python's built-in `hashlib`
* 🔄 Converts text into a hexadecimal hash

---

## ⚙️ How It Works

The toolkit uses a simple **menu-driven architecture**:

```text
USER
 │
 ▼
Display Menu
 │
 ▼
Select Option
 │
 ├──────────────┬──────────────┐
 ▼              ▼              ▼
Password      Password        Hash
Generator     Checker        Generator
 │              │              │
 ▼              ▼              ▼
Generate      Analyze         SHA-256
Password      Strength         Hash
 │              │              │
 └──────────────┴──────────────┘
                │
                ▼
          Return to Menu
```

Each feature is separated into its own function, keeping the program **simple, readable, and maintainable**.

---

## 🧠 Concepts Practiced

| Concept            | Used For                      |
| ------------------ | ----------------------------- |
| `def`              | Creating reusable functions   |
| `if / elif / else` | Program logic                 |
| `while`            | Keeping the toolkit running   |
| `for`              | Iterating through characters  |
| `input()`          | Receiving user input          |
| `try / except`     | Handling invalid input        |
| `secrets`          | Secure random generation      |
| `string`           | Character sets                |
| `hashlib`          | SHA-256 hashing               |
| Boolean variables  | Tracking password criteria    |
| `return`           | Returning generated passwords |

---

## 🚀 Run It

### 1. Clone the repository

```bash
git clone https://github.com/localbtstudio-tech/python-security-toolkit.git
```

### 2. Enter the project

```bash
cd python-security-toolkit
```

### 3. Run the program

```bash
python main.py
```

---

## 🎮 Example

```text
-------------------------------------
|      PYTHON SECURITY TOOLKIT      |
|              V1.1                 |
-------------------------------------

1. Password Generator
2. Password Strength Checker
3. Hash Generator
4. Exit

Choose an option: 1

Enter password length: 16

Generated Password: aB7!xP2@kL9#mQ4$
```

### Password Strength

```text
Choose an option: 2

Enter your password: MyPassword123!

Password Strength: Strong
```

### SHA-256 Hash

```text
Choose an option: 3

Enter text to hash: Hello World

SHA-256: a591a6d40bf420404a011733cfb7b190...
```

---

## 📁 Project Structure

```text
python-security-toolkit/
│
├── main.py
├── README.md
└── .gitignore
```

---

## ◼︎ Why I Built This

This project is part of my **Python learning journey**, focusing on strengthening programming fundamentals while exploring basic **cybersecurity concepts**.

It helped me practice:

**Python → Logic → Functions → Modules → Error Handling → Security Fundamentals**

---

## 🔮 Next Steps

Possible improvements:

* [ ] Improve password strength analysis
* [ ] Add password entropy calculation
* [ ] Add more hashing algorithms
* [ ] Add file hashing
* [ ] Add hash verification
* [ ] Add customizable password generation
* [ ] Improve CLI interface
* [ ] Add automated tests
* [ ] Refactor into multiple modules

---

## ⚠️ Security Note

This project is **educational** and demonstrates basic security concepts.

The password strength checker uses a simple rule-based system and should not be considered a professional password auditing tool.

`SHA-256` is also **not recommended for storing passwords**. Real applications should use dedicated password-hashing algorithms such as `Argon2`, `bcrypt`, or `scrypt`.

---

## 👨‍💻 Author

**Hamza Weslati**

IT Student · Web Developer

[GitHub](https://github.com/localbtstudio-tech)

---

<div align="center">

### 🔐 PYTHON SECURITY TOOLKIT

*Built with Python. Learning security one project at a time.*

**© 2026 Hamza Weslati**

</div>
