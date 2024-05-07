def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_count = count_letters(text)
    char_sorted_list = dict_sorted_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words in this book")
    print()

    for item in char_sorted_list:
        if item ["char"].isalpha() == True:
            print(f"The '{item['char']}' character was found '{item['num']}' times")

   
    print("--- End Report ---")

def word_count(text):
    words = text.split()
    return len(words)   

def sort_on(d):
    return d["num"]

def dict_sorted_list(num_char_dict):
    sorted_list = []
    for c in num_char_dict:
        sorted_list.append({"char": c, "num": num_char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_letters(text):
    counts ={}
    for char in text.lower():
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()




