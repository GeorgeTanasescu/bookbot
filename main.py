print("Hello world")
def count_words_in_string(text):
    return len(text.split())

def count_chars_in_string(text):
    chars_count = {}
    for c in text:
        if c.lower() not in chars_count:
            chars_count[c.lower()] = 1
        else:
            chars_count[c.lower()] += 1
    return chars_count

def convert_to_alpha_list(dict):
    alpha_list = []
    for key in dict:
        if key.isalpha():
            alpha_list.append(f"The key '{key}' character was found {dict[key]} times")
    return alpha_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(str(count_words_in_string(file_contents)) + " words found in document")
        char_dict = count_chars_in_string(file_contents)
        alpha_list = convert_to_alpha_list(char_dict)
        alpha_list.sort()
        for alpha in alpha_list:
            print(alpha)
        print("--- End report ---")
main()
    
