# ZIP Password Recovery

A Python tool that recovers the password of a ZIP file you own but can no longer
open.

## What it does

The tool tries candidate passwords until one opens the archive. It has two
modes:

- Wordlist mode tries each line of a password list, such as rockyou.txt. This is
  fast and matches how real recovery and testing work.
- Brute force mode tries every combination up to a set length. This only works
  for very short passwords, because the number of combinations grows fast.

## What it shows

- Working with the zipfile module and archive internals.
- The difference between wordlist and brute force attacks.
- Careful error handling: it catches only the wrong-password case, not every
  error.

## Features

- Wordlist mode for realistic recovery.
- Brute force mode with an adjustable max length.
- Reports the password found and how many tries it took.

## Install

The zipfile module is part of the standard library, so no install is needed for
modern Python. The requirements file lists a backport only for old versions.

## Usage

```sh
python3 zip_cracker.py secret.zip --wordlist rockyou.txt
python3 zip_cracker.py secret.zip --brute --max-length 4
```

## Sample output

```
Trying passwords from rockyou.txt ...

Password found: dragon123
Tried 8714 candidate(s).
```

## Why it matters

Password cracking shows why weak ZIP passwords are not real protection. A short
or common password falls in seconds. This is the same reason strong, unique
passwords matter everywhere.

## Authorized use only

Use this only on archives you own or are allowed to test, such as recovering
your own file or solving a CTF challenge. Cracking files you do not own is
illegal.
