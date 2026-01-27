
# Password Strength Checker (CLI)

A simple, practical Python command-line tool that scores password strength and provides actionable suggestions. It validates common password quality rules (length, character variety) and rejects passwords found in a large common-password blacklist.

## Why this project

This is a compact security-focused utility that demonstrates:

- CLI design with `argparse`
- Input validation with regular expressions
- Clear, user-friendly feedback output
- Basic security hygiene via a common-password blacklist

## Features

- **Score 0–5** based on five checks:
	- Minimum length (8+ characters)
	- Contains uppercase letter
	- Contains lowercase letter
	- Contains digit
	- Contains special character
- **Blacklist check** against `common_passwords.txt` (case-insensitive)
- **Human-readable rating**: Very Weak → Very Strong
- **Suggestions** explaining exactly what to improve
- Flags **3+ repeated characters in a row** (e.g., `aaab`) and warns against it

## Quick start


```bash
python password_checker.py "MyP@ssw0rd" 
```


## Sample output

```text
========== PASSWORD CHECK ==========
Password Strength: Weak
Score: 2/5

Suggestions:
 - Password is too short (minimum 8 characters).
 - Add at least one uppercase letter.
 - Add at least one digit.
 - Add at least one special character.
===================================
```

## How scoring works

The tool starts at 0 and adds 1 point for each rule satisfied:

- +1 if length ≥ 8
- +1 if contains `[A-Z]`
- +1 if contains `[a-z]`
- +1 if contains `[0-9]`
- +1 if contains a special character from: `!@#$%^&*(),.?":{}|<>`

If the password appears in the blacklist (after lowercasing), the score is set to **0** and a warning is added.

Ratings:

- 5 → Very Strong
- 4 → Strong
- 3 → Moderate
- 2 → Weak
- 0–1 → Very Weak

## Notes and limitations

- This is an educational checker and does **not** estimate real-world crack time.
- The blacklist is a straightforward line-based list; it can be replaced/expanded easily.
- The repeated-character rule currently adds a suggestion but does not reduce the score.

## Learning outcomes

- Building a user-friendly CLI with `argparse` (inputs, help text, predictable output)
- Using `re` effectively for validation rules (character classes and pattern checks)
- Designing scoring logic + actionable feedback messages
- Applying a basic security control (common-password blacklist) with case-insensitive matching

## Ideas for improvement

- Add an optional `--blacklist-path` CLI argument
- Add checks for keyboard patterns and common substitutions (e.g., `P@ssw0rd`)
- Add entropy estimation and crack-time approximations
- Add unit tests for scoring edge cases


