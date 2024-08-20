def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    number_of_words = words_counter(file_contents)
    print(number_of_words)

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

main()