# Password Strength Checker

A Python tool that rates a password and tells you how to make it stronger.

## What it does

The checker looks at five things: length of at least 12 characters, a lowercase
letter, an uppercase letter, a number, and a symbol. It scores the password out
of 5, gives a rating of Weak, Moderate, or Strong, and lists the exact items
that are missing.

Everything runs on your machine. Nothing is stored or sent.

## What it shows

- Password policy logic with regex.
- Clear, actionable feedback instead of a single score.
- A CLI that can take input directly or prompt for it.

## Features

- Scores length and four character classes.
- Explains what to add, item by item.
- Takes the password as an argument or at a prompt.

## Install

No external dependencies. Python 3.8 or newer.

## Usage

```sh
python3 password_checker.py
python3 password_checker.py --password "CorrectHorse9!"
```

## Sample output

```
Strength: Moderate (3/5)
How to improve:
  - Add at least 12 characters.
  - Add a symbol.
```

## Notes

- This checks structure, not whether a password has leaked. A long, unique
  passphrase from a password manager is still the best practice.
