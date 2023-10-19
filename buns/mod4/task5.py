def take_key(element):
    return element[1]

def ltr_rate(text):
    dict_ltr = {}
    for i in text:
        if i in dict_ltr:
            dict_ltr[i] += 1
        else:
            dict_ltr[i] = 1
    return dict_ltr

def get_path_file(name_file):
    path_file = name_file.split('\\')
    path_file = "\\".join(path_file[:-1])
    return path_file

def filter_ltr(text):
    new_text = filter(str.isalpha, text)
    text = "".join(new_text)
    return text

name_file = input('Введите полное имя файла с расположением: ')

with open(name_file, "r" ) as file:
    text = file.read()

text = filter_ltr(text)
dict_ltr = ltr_rate(text)
sort_list_ltr = sorted(dict_ltr.items(), key=take_key)

new_file = open("\\".join([get_path_file(name_file), "letters rate.txt"]), "w")
for i in sort_list_ltr:
    new_file.write(i[0] + ":" + str(i[1]) + " ")
new_file.close()