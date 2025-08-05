# git_playground
An exploration of re-writing example git hooks in Python

## Setup
Run `.setup.sh` from the root of an initialized git repo with the `git-hooks` directory copied to the root

## Scripts

### pre-commit.py
[pre-commit.sample](git-hooks/pre-commit.sample) re-written in [Python](git-hooks/pre-commit.py)

*Test Cases*

1) set `git config --bool hooks.allownonascii false`, add a non-ascii file, `hы.txt` and notice error message
2) add white spaces and extra lines to end of files and notice error messages
