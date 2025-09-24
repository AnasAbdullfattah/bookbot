def get_num_words(file_path):
    with open(file_path, "r") as the_book:
        file_contents = the_book.read()
        words_of_book = file_contents.split()
        print(f"Found {len(words_of_book)} total words")

