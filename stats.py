def get_book_text (the_filepath):
    with open(the_filepath) as f:
        file_contents = f.read()
        return file_contents


def get_num_words(the_filepath):
    with open(the_filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.split()
        words_count = len(file_contents)
        return words_count


def chareacters_counter(the_filepath):
    the_dictionary = {}
    with open(the_filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for i in file_contents:
            if i in the_dictionary:
                the_dictionary[i] = the_dictionary[i]+1
            else:
                the_dictionary[i] = 1

        return the_dictionary
    


# the report functions


def chareacters_counter(the_filepath):
    the_dictionary = {}
    with open(the_filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for i in file_contents:
            if i.isalpha():
                if i in the_dictionary:
                    the_dictionary[i] = the_dictionary[i]+1
                else:
                    the_dictionary[i] = 1
        return the_dictionary
    

def sort_on(items):
    return items["num"]


def generate_report(the_filepath):
    the_list = []
    the_final_dectioary = chareacters_counter(the_filepath)
    # the_final_dectioary =  sorted(the_final_dectioary, key=lambda x: x['num'], reverse=True)
    for i in the_final_dectioary:
        the_list.append({"char": i, "num": the_final_dectioary[i]})
    the_list.sort(reverse=True, key=sort_on)
    return the_list

