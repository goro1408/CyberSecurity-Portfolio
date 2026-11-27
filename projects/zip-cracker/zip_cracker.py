#!/usr/bin/env python3
"""ZIP Password Recovery.

Recovers the password of a ZIP file you own but have lost access to. It tries
candidate passwords until one opens the archive.

Two modes:
  - Wordlist: try each line of a password list. Fast and realistic.
  - Brute force: try every combination up to a length. Only good for very short
    passwords, since the work grows fast.

Authorized use only. Use this only on archives you own or are allowed to test,
for example recovering your own file or a CTF challenge.

Usage:
    python3 zip_cracker.py secret.zip --wordlist rockyou.txt
    python3 zip_cracker.py secret.zip --brute --max-length 4
"""

import argparse
import itertools
import string
import sys
import zipfile


def try_password(zip_ref, password):
    """Return True if password opens the archive.

    ZIP uses the wrong-password case as a RuntimeError, so we catch only that
    and the bad-zip case. Any other error should surface, not be swallowed.
    """
    try:
        zip_ref.read(zip_ref.namelist()[0], pwd=password.encode())
        return True
    except (RuntimeError, zipfile.BadZipFile):
        return False


def crack_with_wordlist(zip_path, wordlist_path):
    """Try each password in a wordlist file."""
    with zipfile.ZipFile(zip_path) as zip_ref:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as words:
            for count, line in enumerate(words, start=1):
                password = line.strip()
                if not password:
                    continue
                if try_password(zip_ref, password):
                    return password, count
    return None, None


def crack_brute_force(zip_path, max_length, charset):
    """Try every combination of charset up to max_length."""
    tried = 0
    with zipfile.ZipFile(zip_path) as zip_ref:
        for length in range(1, max_length + 1):
            for combo in itertools.product(charset, repeat=length):
                password = "".join(combo)
                tried += 1
                if try_password(zip_ref, password):
                    return password, tried
    return None, tried


def parse_args():
    parser = argparse.ArgumentParser(
        description="Recover the password of a ZIP file you own."
    )
    parser.add_argument("zipfile", help="Path to the password-protected ZIP")
    parser.add_argument(
        "-w", "--wordlist", help="Path to a wordlist file (one password per line)"
    )
    parser.add_argument(
        "-b", "--brute", action="store_true", help="Use brute force instead"
    )
    parser.add_argument(
        "-m", "--max-length", type=int, default=4,
        help="Max length for brute force (default: 4)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.wordlist and not args.brute:
        sys.exit("Choose a mode: --wordlist FILE or --brute")

    if args.wordlist:
        print(f"Trying passwords from {args.wordlist} ...")
        password, count = crack_with_wordlist(args.zipfile, args.wordlist)
    else:
        charset = string.ascii_lowercase + string.digits
        print(f"Brute forcing up to length {args.max_length} ...")
        password, count = crack_brute_force(args.zipfile, args.max_length, charset)

    if password is not None:
        print(f"\nPassword found: {password}")
        print(f"Tried {count} candidate(s).")
    else:
        print("\nPassword not found.")


if __name__ == "__main__":
    main()
