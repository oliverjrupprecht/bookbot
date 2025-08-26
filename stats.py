def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(filepath):
    file_contents = get_book_text(filepath)
    count = 0
    split_into_words = file_contents.split()
    for i in range(0, len(split_into_words)):
        count += 1

    return count

def get_num_characters(filepath):
    file_contents = get_book_text(filepath)

    count = {}
    
    for char in file_contents:
        low = char.lower()
        if low not in count:
            count[low] = 1
        else: 
            count[low] += 1

    return count

def make_new_dict(dict):
    list = []

    for key in dict:
        new_dict = {}
        if key not in new_dict:
            new_dict["char"] = key
            new_dict["num"] = dict[key]
            list.append(new_dict)

    return list

def sort_on(dict):
    return dict["num"]

def sort_by_apperance(dict):

    new_dict = make_new_dict(dict)

    new_dict.sort(reverse=True, key=sort_on)

    return new_dict

