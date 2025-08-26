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
