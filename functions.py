import csv
import re

def read_csv(csv_file):
    with open(csv_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def write_csv(csv_file, data_list):
    with open(csv_file, "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(data_list)
    return

def subst(string, pattern, substitution):
    pattern = pattern
    subst = substitution
    correct_text = re.sub(pattern, subst, string)
    return correct_text

def union(list):
    result_list = []
    new_str = ""
    for el in list:
        lastname = el[0]
        firstname = el[1]
        surname = el[2]
        organization = el[3]
        pozition = el[4]
        phone = el[5]
        e_mail = el[6]

        if lastname + firstname not in new_str:
            new_str += lastname + firstname
            result_list.append(el)
        else:
            for el in result_list:
                if el[0] == lastname and el[1] == firstname:
                    if len(el[2]) < 2:
                        el[2] = surname
                    if len(el[3]) < 2:
                        el[3] = organization
                    if len(el[4]) < 2:
                        el[4] = pozition
                    if len(el[5]) < 2:
                        el[5] = phone
                    if len(el[6]) < 2:
                        el[6] = e_mail
    return result_list