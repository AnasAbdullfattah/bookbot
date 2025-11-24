import sys
from stats import get_num_words
from stats import generate_report




def main():
    # the_filepath ="./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        the_filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        char_count = get_num_words(the_filepath)
        print(f"Found {char_count} total words")
        print("--------- Character Count -------")
        the_sorted_report = generate_report(the_filepath)
        for i in the_sorted_report:
            print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
        

main()
