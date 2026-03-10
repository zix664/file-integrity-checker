import hashlib
import os
import fnmatch


def load_ignore_patterns(ignore_file="ignore.txt"):

    patterns = []

    if os.path.exists(ignore_file):

        with open(ignore_file, "r") as f:

            for line in f:

                pattern = line.strip()

                if pattern:
                    patterns.append(pattern)

    return patterns


def should_ignore(filepath, patterns):

    for pattern in patterns:

        if fnmatch.fnmatch(filepath, pattern) or pattern in filepath:
            return True

    return False


def hash_file(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:

        while True:

            chunk = f.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def hash_directory(directory):

    hashes = {}

    ignore_patterns = load_ignore_patterns()

    for root, dirs, files in os.walk(directory):

        for file in files:

            filepath = os.path.join(root, file)

            if should_ignore(filepath, ignore_patterns):
                continue

            file_hash = hash_file(filepath)

            hashes[filepath] = file_hash

    return hashes