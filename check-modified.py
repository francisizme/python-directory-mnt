import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    readable_date = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return f'{readable_date.year}-{readable_date.month}-{readable_date.day}'


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
