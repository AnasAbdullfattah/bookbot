def get_num_words(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read()
        words_of_book = file_contents.split()
        words_number= len(words_of_book)
        # print(f"Found {len(words_of_book)} total words")
        return words_number


def return_txt(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read().lower()
        return file_contents
    
# def split_txt(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read().lower()
        words_of_book = file_contents.split()
        return words_of_book


def charachter_dictionary(file_path):
    the_contents = return_txt(file_path)
    dictionary = {}

    for i in the_contents:
        if i.isalpha():
            if (i not in dictionary):
                dictionary[i] = 1
            else:
                dictionary[i] += 1
    return dictionary



def report(file_path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    char_num = get_num_words(file_path)
    print(f"Found {char_num} total words")
    print("--------- Character Count -------")
    the_dictionary = charachter_dictionary(file_path)
    # myKeys = list(the_dictionary.keys())
    # myKeys.sort()
    # sdicrionery = {i: the_dictionary[i] for i in myKeys}

    sorted_items_desc = sorted(the_dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dict_desc = dict(sorted_items_desc)
    print(sorted_dict_desc)
    print("============= END ===============")
    return 0

    