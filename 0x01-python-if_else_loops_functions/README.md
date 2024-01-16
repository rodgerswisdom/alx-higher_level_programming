# Project README.md

## Python - if/else, loops, functions

### Project Overview

This project focuses on Python programming fundamentals, covering topics such as control flow (if/else statements, loops), functions, and basic arithmetic operations. The goal is to reinforce understanding of these concepts and build a solid foundation for more advanced programming.

### Project Details

- **Project Start Date:** Jan 16, 2024 6:00 AM
- **Project End Date:** Jan 17, 2024 6:00 AM
- **Checker Release Date:** Jan 16, 2024 12:00 PM
- **Auto Review Deadline:** Jan 17, 2024

### Resources

Before starting the tasks, it's recommended to read or watch the following resources:

- [More Control Flow Tools](#) (Read until "4.6. Defining Functions" included)
- [IndentationError](#)
- [How To Use String Formatters in Python 3](#)
- [Learn to Program](#)
- [Learn to Program 2: Looping](#)
- [Pycodestyle – Style Guide for Python Code](#)

### Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome.
- Understand the importance of indentation in Python.
- Use if, if...else statements effectively.
- Apply comments in your code.
- Assign values to variables and manipulate them.
- Utilize while and for loops in Python.
- Compare Python's for loop with C's.
- Employ break and continue statements.
- Work with else clauses in loops.
- Understand the purpose of the pass statement.
- Use the range function.
- Comprehend what a function is and how to use functions.
- Explain the return of a function that does not use any return statement.
- Understand the scope of variables.
- Recognize what a traceback is.
- Familiarize yourself with arithmetic operators and their usage.

### Project Requirements

#### Python Scripts

- **Allowed Editors:** vi, vim, emacs
- **Interpretation/Compilation:** Ubuntu 20.04 LTS using python3 (version 3.8.5)
- **File Requirements:**
  - All files must end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - A README.md file at the root of the project folder is mandatory.
  - Code should adhere to Pycodestyle (version 2.8.*).
  - All files must be executable.
- **Length of Files:** The length of your files will be tested using wc.

#### C Scripts

- **Allowed Editors:** vi, vim, emacs
- **Compilation:** Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- **File Requirements:**
  - All files must end with a new line.
  - Your code should use the Betty style, checked using betty-style.pl and betty-doc.pl.
  - Not allowed to use global variables.
  - No more than 5 functions per file.
  - Prototypes of all functions should be included in a header file named lists.h.
  - Don't forget to push your header file.
  - All header files should be include guarded.

### Tasks

#### Task 0: Positive anything is better than negative nothing

This program assigns a random signed number to the variable `number` each time it is executed. Complete the source code to print whether the number is positive or negative.

Example output:
```bash
$ ./0-positive_or_negative.py
-4 is negative
$ ./0-positive_or_negative.py
0 is zero
$ ./0-positive_or_negative.py
-3 is negative
...
```

**Repo:**
[alx-higher_level_programming/0x01-python-if_else_loops_functions/0-positive_or_negative.py](#)

#### Task 1: The last digit

This program assigns a random signed number to the variable `number` each time it is executed. Complete the source code to print the last digit of the number.

Example output:
```bash
$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
...
```

**Repo:**
[alx-higher_level_programming/0x01-python-if_else_loops_functions/1-last_digit.py](#)

#### Task 2: I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

Write a program that prints the ASCII alphabet in lowercase, not followed by a new line.

Example output:
```bash
$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz
```

**Repo:**
[alx-higher_level_programming/0x01-python-if_else_loops_functions/
