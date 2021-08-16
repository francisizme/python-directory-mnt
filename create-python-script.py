def create_python_script(filename):
    comments = [
        "#!/usr/bin/env python3",
        "# Start of a new Python program",
        "print('Hello')",
    ]
    with open(filename, 'w') as file:
        for line in comments:
            file.write(line + '\n')
        filesize = file.tell()
    return filesize


print(create_python_script("program.py"))
