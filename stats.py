def get_num_words(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read()
        words_of_book = file_contents.split()
        # print(f"Found {len(words_of_book)} total words")
        return words_of_book


def return_txt(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read()
        # words_of_book = file_contents.split()
        # print(f"Found {len(words_of_book)} total words")
        return file_contents


def charachter_dictionary(file_path):
    the_contents = get_num_words(file_path).lower()
    dictionary = {}

    for i in the_contents:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary



def report(file_path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    # char_num = get_num_words(file_path)
    # print(f"Found {char_num} total words")
    # print("--------- Character Count -------")
    # the_dictionary = charachter_dictionary(file_path)
    # new_dictionary = sorted(the_dictionary, key=int)
    # print(new_dictionary)
    print("============= END ===============")
    return 0

    