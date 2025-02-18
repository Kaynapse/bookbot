def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words = word_count(book_text)
    
    alphabet_count = letter_amount(book_text)
    dict_list = convert_dict_to_dict_list(alphabet_count)
    print_report(dict_list)


# counts the amount of words in a text string, returns int value 
def word_count(text_string):
    words = text_string.split()
    return len(words)

#extract string from file path
def get_book_text(path):
    with open(path) as f:
        return f.read()

# count the amount of each letter used in text string    
def letter_amount(text_string):
    lower_case_string = text_string.lower()
    alphabet_count = {}
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '?', " "]
    for letter in alphabet:
        if letter.isalpha():
            letter_count = lower_case_string.count(letter)
            alphabet_count[letter] = letter_count
        
        
    return alphabet_count

def convert_dict_to_dict_list(dictionary):
    dict_list = []
    for entry in dictionary:
        entry_dict = {

        }
        entry_dict["letter"] = entry
        entry_dict["num"] = dictionary[entry]
        dict_list.append(entry_dict)
    dict_list.sort(reverse=True, key=sort_on)
        
    
    return dict_list

# function that returns the num key value of a dictionary    
def sort_on(dict):
    return dict["num"]        

def print_report(dict_list):
    for dictionary in dict_list:
        
        print(f"The '{dictionary['letter']}' character was found {dictionary['num']} times")

main()