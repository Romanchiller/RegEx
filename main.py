import functions as f

result = []
pattern1 = r'(\+?\d)\s?\(?(\d{3})\)?[\s?\-]?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?([\д\о\б\.]+)?\s?(\d{4})?\)?'
subst1 = r'+7(\2)\3-\4-\5 \6 \7'

pattern2 = r"([А-Я][а-я]+)[\s\,]?([А-Я][а-я]+)([\s\,]?)([А-Я][а-я]+)?(\,+?)"
subst2 = r"\1, \2, \4, "

pattern3 = r"([А-Я][а-я]+)(\,\s)([А-Я][а-я]+)(\,\s)([А-Я][а-я]+)?([\,\s]+)([А-я]+)?(,+)?([\w\s–]+)?,?(\+7\(\d+\)\d+-\d+-\d+)?([\s,]+)?([доб\.]+\s\d+)?,([A-z@\.1-9]+)?"
subst3 = r"\1, \3, \5, \7, \9, \10 \12, \13"

if __name__ == '__main__':
    contact_list = f.read_csv("phonebook_raw.csv")
    for el in contact_list:
        string_el = ",".join(el)
        phone_correct = f.subst(string_el, pattern1, subst1 )
        name_correct = f.subst(phone_correct, pattern2, subst2)
        all_correct = f.subst(name_correct, pattern3, subst3)

        correct_list = all_correct.split(",")
        result.append(correct_list)

    union = f.union(result)

    f.write_csv('phonebook.csv', union)
