
```markdown
# 0. Run Python file

## Task Description
Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

## Example
```bash
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

## Repository Information
- **GitHub Repository:** [alx-higher_level_programming](https://github.com/rodgerswisdom/alx-higher_level_programming.git)
- **Directory:** 0x00-python-hello_world
- **File:** 0-run

## Instructions
1. **Shell Script:**
   - Write a Shell script to execute a Python script.
   - Save the Python file name in the environment variable `$PYFILE`.

2. **Execution:**
   - Run the script and observe the output.
   - Ensure that the Python file is executed as expected.

## Project Structure
```
alx-higher_level_programming/
└── 0x00-python-hello_world/
    └── 0-run
```

## Completion
Follow the provided example and instructions to create a Shell script that successfully executes the specified Python file.

If you have any questions or need assistance, feel free to ask.
```


