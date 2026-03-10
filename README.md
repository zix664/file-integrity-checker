# File Integrity Checker

A Python-based security tool that monitors file integrity using cryptographic hashes.

The tool creates a baseline of file hashes for a directory and later verifies whether any files have been modified, deleted, or added. This technique is commonly used in **Host Intrusion Detection Systems (HIDS)**.

---

## Features

* SHA256 cryptographic hashing
* Recursive directory scanning
* Integrity verification
* Detection of:

  * Modified files
  * Deleted files
  * Newly added files
* Command-line interface (CLI)
* Ignore rules for unnecessary files

---

## How It Works

1. The tool scans a directory and computes SHA256 hashes for all files.
2. The hashes are stored in a database file (`hashes.json`).
3. During verification, the tool recalculates hashes and compares them with the stored values.
4. Any differences indicate potential file tampering.

---

## Project Structure

```
file-integrity-checker
│
├── fic.py                # Main CLI tool
├── directory_hasher.py   # File hashing and directory scanning
├── ignore.txt            # Patterns of files to ignore
├── README.md
└── .gitignore
```

---

## Requirements

* Python 3.x
* Standard Python libraries only (`hashlib`, `os`, `json`, `argparse`)

No external dependencies are required.

---

## Usage

### Create Baseline Database

```
python fic.py init <directory>
```

Example:

```
python fic.py init test_folder
```

This creates the file:

```
hashes.json
```

which stores the baseline hashes.

---

### Verify File Integrity

```
python fic.py check <directory>
```

Example output:

```
--- Integrity Check Report ---

Modified: config.txt
Deleted: notes.txt
New File: malware.exe
```

---

## Ignore Rules

Files listed in `ignore.txt` will be skipped during hashing.

Example:

```
*.log
*.tmp
*.pyc
__pycache__
```

---

## Use Cases

* Detect unauthorized file modifications
* Monitor important system files
* Learn about cryptographic hashing and filesystem security

---

## Future Improvements

Possible enhancements:

* Support for multiple hashing algorithms
* Colored terminal output
* Packaging as a Python CLI tool
* Scheduled integrity checks

---

## License

This project is open source and available under the MIT License.
