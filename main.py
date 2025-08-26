from stats import get_num_words
from stats import get_num_characters

def main():
    print(f"{get_num_words("books/frankenstein.txt")} words found in the document")

    print(get_num_characters("books/frankenstein.txt"))


main()

