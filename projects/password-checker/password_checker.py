#!/usr/bin/env python3
"""Password Strength Checker.

Rates a password and explains what would make it stronger. It checks length and
character variety, scores the password, and prints clear feedback.

This is a teaching tool about password hygiene. It does not store or send
anything. Everything runs locally.

Usage:
    python3 password_checker.py
    python3 password_checker.py --password "CorrectHorse9!"
"""

import argparse
import re

SYMBOLS = r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>/?\\|`~]"


def analyze_password(password):
    """Score a password and return (rating, score, feedback list)."""
    checks = {
        "at least 12 characters": len(password) >= 12,
        "a lowercase letter": re.search(r"[a-z]", password) is not None,
        "an uppercase letter": re.search(r"[A-Z]", password) is not None,
        "a number": re.search(r"\d", password) is not None,
        "a symbol": re.search(SYMBOLS, password) is not None,
    }

    score = sum(checks.values())
    feedback = [f"Add {name}." for name, passed in checks.items() if not passed]

    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, score, feedback


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check the strength of a password."
    )
    parser.add_argument(
        "-p", "--password",
        help="Password to check. If omitted, you are prompted for it.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    password = args.password
    if not password:
        password = input("Enter a password to check: ")

    rating, score, feedback = analyze_password(password)

    print(f"\nStrength: {rating} ({score}/5)")
    if feedback:
        print("How to improve:")
        for item in feedback:
            print(f"  - {item}")
    else:
        print("This password meets every check.")


if __name__ == "__main__":
    main()
