# Password Generator

A simple yet powerful password generator tool that creates secure, random passwords with customizable length and character sets.

## Features

- 🔒 Generate strong, random passwords
- ⚙️ Customize password length (4-256 characters)
- 🔠 Multiple character sets:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (!@#$...)
- 📝 Generate multiple passwords at once
- 💾 Save passwords to a text file (default location: `/sdcard/Download/generated_passwords.txt`)
- 🖥️ Simple command-line interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bjmdevelopers/Password-Generator.git
   cd password-generator
   ```

2. Run the script:
   ```bash
   python password_generator.py
   ```

## Usage

1. Run the script
2. Follow the interactive prompts:
   - Enter password length (default: 16)
   - Select character sets to include
   - Specify how many passwords to generate
   - Choose whether to save to a file
3. Your secure passwords will be displayed and optionally saved

## Requirements

- Python 3.x

## Screenshot

```
╭───────────────────────────────╮
│      PASSWORD GENERATOR       │
╰───────────────────────────────╯

Password length (default 16): 12
Include uppercase letters (A-Z)? [Y/n]: y
Include lowercase letters (a-z)? [Y/n]: y
Include numbers (0-9)? [Y/n]: y
Include symbols (!@#$...)? [Y/n]: y

How many passwords to generate (default 1): 3

╭───────────────────────────────╮
│ Xk7#pL9@qR2$
│ 8mN!3vZ*6bW%
│ Hj5^dK8&fG9#
╰───────────────────────────────╯

Save passwords to .txt file and download? [Y/n]: y

✅ Saved to: /sdcard/Download/generated_passwords.txt

Generate more? [Y/n]: n
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

🔐 Generate strong passwords and stay secure!
