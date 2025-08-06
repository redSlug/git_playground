#!/usr/bin/python3

import subprocess
import sys

SUCCESS_RETURN_CODE = 0
ASCII_ERROR_MESSAGE = '''
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
'''

repo_has_no_commits = subprocess.run(
    "git rev-parse --verify HEAD >/dev/null 2>&1",
    shell=True,
).returncode != SUCCESS_RETURN_CODE

against = 'HEAD'

if repo_has_no_commits:
    # diff against an empty tree object
    against = subprocess.run(
        "git hash-object -t tree /dev/null",
        shell=True,
        capture_output=True,
         text=True
    ).stdout

require_ascii = subprocess.run(
    "git config --type=bool hooks.allownonascii",
    shell=True,
    capture_output=True,
    text=True
).stdout != 'true\n'

if require_ascii:
    file_names_are_ascii = subprocess.run(
        "git diff-index --cached --name-only --diff-filter=A -z " + against,
        shell=True,
        capture_output=True,
        text=True
    ).stdout.isascii()

    if not file_names_are_ascii:
        print(ASCII_ERROR_MESSAGE, file=sys.stderr)
        exit(1)


error_message = subprocess.run(
    "git diff-index --check --cached " + against,
    shell=True,
    capture_output=True,
    text=True
).stdout

if error_message:
    print(error_message, file=sys.stderr)
    exit(1)
