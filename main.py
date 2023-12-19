import os

directory = os.getcwd()
content = os.listdir(directory)
txt = []
direct = {}
new_file = {}

for files in content:
    if os.path.isfile(os.path.join(directory, files)) and files.endswith('.txt'):
        txt.append(files)

for file in txt:
    with (open(file, 'r', encoding='UTF-8') as f):
        data = f.read()
        count = 0
    for line in data.split('\n'):
        count += 1
    new_file[file] = data
    direct[file] = count
answer = sorted(direct.items(), key=lambda item: item[1], reverse=False)
my_txt = open('new_txt.txt', 'w', encoding='UTF-8')
for new_text in answer:
    name_file = new_text[0]
    count_line = new_text[1]
    text_new = str(new_file.get(new_text[0])) + str("\n")
    my_txt.write(name_file + "\n" + str(count_line) + "\n" + text_new + "\n")
my_txt.close()









