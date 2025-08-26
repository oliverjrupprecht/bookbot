from stats import get_num_words
from stats import get_num_characters
from stats import make_new_dict
from stats import sort_by_apperance

def main():
    filepath = "books/frankenstein.txt"
    cleaned = sort_by_apperance(get_num_characters(filepath))
    wordcount = get_num_words(filepath)

    print(f"============ BOOKBOT ============\nAnlyzing book found at {filepath}")
    print(f"----------- Word Count ----------\nFound {wordcount} total words")
    print(f"--------- Character Count -------")
    
    for dict in cleaned:
        print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()

