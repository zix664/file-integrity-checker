import argparse
import json
from directory_hasher import hash_directory


def create_database(directory, db_file="hasher.json"):

    hashes = hash_directory(directory)

    with open(db_file, "w") as f:
        json.dump(hashes, f, indent=4)

    print("Integrity database created")


def verify_integrity(directory, db_file="hasher.json"):

    with open(db_file, "r") as f:
        saved_hashes = json.load(f)

    current_hashes = hash_directory(directory)

    print("\n--- Integrity Check Report ---\n")

    for file in saved_hashes:

        if file not in current_hashes:
            print("Deleted:", file)

        elif saved_hashes[file] != current_hashes[file]:
            print("Modified:", file)

    for file in current_hashes:

        if file not in saved_hashes:
            print("New File:", file)


def main():

    parser = argparse.ArgumentParser(description="File Integrity Checker")

    parser.add_argument("command", choices=["init", "check"],
                        help="init = create database, check = verify integrity")

    parser.add_argument("directory", help="directory to scan")

    args = parser.parse_args()

    if args.command == "init":
        create_database(args.directory)

    elif args.command == "check":
        verify_integrity(args.directory)


if __name__ == "__main__":
    main()