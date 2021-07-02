#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start of each line of text on the clipboard
# this program is written by me with criteria taken from the ATBS project (pg. 147)

import pyperclip

out = []
text = pyperclip.paste()
lines = text.split('\n')

for line in lines:
    out.append('* ' + str(line))
    print(line)
    print('space')

text = '\n'.join(out)
pyperclip.copy(text)
print('The bulleted text has been copied to the clipboard.')