Introduction to Git
===================

2013-09-05
----------

### Commits

Commit messages

* A very descriptive account of the change(s) made
* Present tense only!!
* Simple messages are one-liners (less than 50 characters)
* Complex messages use more lines (blank, then 72 chars or less)
* Single line can be added with git commit -m 'Message here.'
* Multiple lines can be added with git commit (launches an editor)

### Three Trees

* Repository (repo)
* Staging Index
* Working Directory (wd)

Actions

Checkout: Repository -> Working Directory (git init|clone|checkout)
Stage: Working Directory -> Staging Index (git add)
Commit: Staging Index -> Repository (git commit)

### Git Workflows

#### New file

    Create/copy file into wd
    git add filename.ext
    git commit -m 'Commit message.'

#### Edit file

    Edit file in wd
    git add filename.ext
    git commit -m 'Commit message.'

#### Creating a git repository

    $ mkdir secondgit           # Create a directory
    $ cd secondgit              # Enter the new directory
    $ git init

### Configuration

    git config

In decreasing precedence

* Local (This repo)
* Global (This user)
* System (This machine)

2013-09-09
----------

### File management

* Renaming files (git mv)
* Deleting files (git rm)

### Remotes

#### GitHub.com

