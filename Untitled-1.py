import os

files = os.listdir('.')

for file in files:
    with open(file, 'r', encoding='ansi') as f:
        text = f.read()

# process Unicode text

    with open(file, 'w', encoding='utf8') as f:
        f.write(text)


