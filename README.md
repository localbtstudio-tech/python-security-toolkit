# PYTHON SECURITY TOOLKIT 🔐

<div align="center">

### A lightweight command-line security toolkit built with Python.

**Python · Security Fundamentals · Networking · Cryptography · CLI**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Security-black?style=for-the-badge)
![Networking](https://img.shields.io/badge/Networking-TCP-005571?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

</div>

---

## ◼︎ The Project

A simple but structured **command-line security toolkit** built from scratch with Python.

The toolkit brings together several practical security utilities in one application, including **password generation, password strength checking, hashing, Base64 encoding/decoding, file hashing, and TCP port scanning**.

The goal was to practice Python programming while exploring fundamental concepts related to **security, cryptography, file handling, and networking**.

> **Small project. Real fundamentals.**

---

## ✦ What It Can Do

```text
┌─────────────────────────────────────┐
│       PYTHON SECURITY TOOLKIT       │
├─────────────────────────────────────┤
│  1. Password Generator              │
│  2. Password Strength Checker       │
│  3. Hash Generator                  │
│  4. File Hashing                    │
│  5. Encode / Decode                 │
│  6. Port Scanner                    │
│  7. Exit                            │
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
* 📊 Classifies passwords as Weak, Medium, or Strong

### #️⃣ Hash Generator

* 🔐 Generates SHA-256 hashes
* ⚡ Uses Python's `hashlib`
* 🔄 Converts text into a hexadecimal hash

### 📁 File Hashing

* 📄 Reads files in binary mode
* 🔐 Generates a SHA-256 hash for the file
* ❌ Handles missing files
* 🔎 Useful for understanding file integrity

### 🔄 Encode / Decode

* 🔤 Base64 encoding
* 🔓 Base64 decoding
* ❌ Handles invalid Base64 input
* 🧩 Uses `base64` and `binascii`

### 🌐 Port Scanner

* 🔎 Scans a custom port range
* 🌐 Accepts a target IP address
* 🔌 Uses TCP connections
* ⏱️ Uses connection timeouts
* 🟢 Displays open ports
* 📡 Uses Python's `socket` module

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
 ├──────────────┬──────────────┬──────────────┐
 ▼              ▼              ▼              ▼
Password      Password        Hash          File
Generator     Checker        Generator      Hashing
 │              │              │              │
 └──────────────┴──────────────┴──────────────┘
 │
 ├──────────────┬──────────────┐
 ▼              ▼              ▼
Encode/Decode  Port Scanner    Exit
 │              │
 ▼              ▼
Base64        TCP Scan
 │              │
 └──────────────┴──────────────┐
                               ▼
                         Return to Menu
```

Each feature is separated into its own function, keeping the program **simple, readable, and maintainable**.

---

## 🧠 Concepts Practiced

| Concept            | Used For                               |
| ------------------ | -------------------------------------- |
| `def`              | Creating reusable functions            |
| `if / elif / else` | Program logic                          |
| `while`            | Menu and sub-menu loops                |
| `for`              | Iterating through ports and characters |
| `input()`          | Receiving user input                   |
| `try / except`     | Handling invalid input and errors      |
| `secrets`          | Secure random password generation      |
| `string`           | Character sets                         |
| `hashlib`          | SHA-256 hashing                        |
| `base64`           | Base64 encoding and decoding           |
| `binascii`         | Handling Base64 errors                 |
| `socket`           | Network communication                  |
| `SOCK_STREAM`      | TCP stream sockets                     |
| `connect_ex()`     | Checking TCP connections               |
| File handling      | Reading files for hashing              |
| `settimeout()`     | Controlling socket connection time     |

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

### Password Generator

```text
Choose an option: 1

Enter password length: 16

Generated Password: aB7!xP2@kL9#mQ4$
```

### File Hashing

```text
Choose an option: 4

Enter file name: test.txt

SHA-256: 9f86d081884c7d659a2feaa0c55ad015...
```

### Encode / Decode

```text
Choose an option: 5

--- Encode / Decode ---
1. Encode
2. Decode
3. Back

Choose an option: 1

Enter text: Hello World

Encoded: SGVsbG8gV29ybGQ=
```

### Port Scanner

```text
Choose an option: 6

Enter target IP: 127.0.0.1
Enter start port: 20
Enter end port: 100

Port 80 is OPEN
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

This project is part of my **Python learning journey**, focusing on strengthening programming fundamentals while exploring practical **cybersecurity concepts**.

The project allowed me to move beyond basic Python exercises and work with:

**Python → Modules → File Handling → Cryptography → Encoding → Networking**

It also gave me practical experience working with Python's standard library and building a multi-feature command-line application.

---

## 🔮 Next Steps

Possible improvements:

* [ ] Improve password strength analysis
* [ ] Add password entropy calculation
* [ ] Add more hashing algorithms
* [ ] Add hash verification
* [ ] Add file integrity comparison
* [ ] Add more encoding methods
* [ ] Improve port scanner performance
* [ ] Add service detection
* [ ] Improve CLI interface
* [ ] Add automated tests
* [ ] Refactor into multiple modules

---

## ⚠️ Security Note

This project is **educational** and demonstrates basic security and networking concepts.

The port scanner should only be used on **systems and networks you own or have explicit permission to test**.

The password strength checker is a simple rule-based system and is not a professional password auditing tool.

`SHA-256` is a cryptographic hash function and should **not** be used directly for storing user passwords. Real applications should use dedicated password-hashing algorithms such as `Argon2`, `bcrypt`, or `scrypt`.

Base64 is an **encoding format, not encryption**. It does not provide confidentiality.

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
