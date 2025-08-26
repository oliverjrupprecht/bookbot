def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def num_words(file_contents):
    count = 0
    split_into_words = file_contents.split()
    for i in range(0, len(split_into_words)):
        count += 1

    return count


def main():
    print(f"{num_words(get_book_text("books/frankenstein.txt"))} words found in the document")


main()

