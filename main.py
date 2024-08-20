def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)

    num_words = words_counter(file_contents)
    char_count = character_counter(file_contents)
    char_list = dict_to_listofdicts(char_count)

    print_report(file_path, num_words, char_list)

def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def words_counter(file_contents):
    words = file_contents.split()
    n = 0
    for word in words:
        n += 1
    return n

def character_counter(file_contents):
    words = file_contents.split()
    char_count = {}

    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char not in char_count:
                char_count[lower_char] = 1
            else:
                char_count[lower_char] += 1
    
    return char_count

def dict_to_listofdicts(dict):
    list = []
    for key in dict:
        new_dict = {}
        new_dict["character"] = key
        new_dict["num"] = dict[key]
        list.append(new_dict)
        list.sort(reverse=True, key=sort_on)
    
    return list

def sort_on (dict):
    return dict["num"]

def print_report(file_path, num_words, list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for dict in list:
        if dict["character"].isalpha():
            print(f"The '{dict["character"]}' character was found {dict["num"]} times")
    
    print("--- End report ---")

    

main()