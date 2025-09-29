# def split_txt(file_path):
#     with open(file_path, "r") as the_book:
#         file_contents = the_book.read().lower()
#         words_of_book = file_contents.split()
#         return words_of_book
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


def get_num(item_dict):
    return item_dict["num"]


def get_sorted_char_counts(char_counts_dict):
  
    # 1. Create the list of dictionaries
    sorted_list = []
    for char, count in char_counts_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=get_num, reverse=True)
    
    return sorted_list











def report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_num = get_num_words(file_path)
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    the_dictionary = charachter_dictionary(file_path)
    the_list = get_sorted_char_counts(the_dictionary)
    for item in the_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return 0
    