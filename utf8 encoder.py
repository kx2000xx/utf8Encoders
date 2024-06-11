import pathlib

files = list(pathlib.Path('myFiles').rglob('*'))
fileslist = []
for item in files:
    if item.is_file():
        fileslist.append(item)
print(fileslist)


for file in fileslist:
    try:
        with open(file, 'r', encoding='ansi') as f:
            text = f.read()


        with open(file, 'w', encoding='utf8') as f:
            f.write(text)
    except:
        pass