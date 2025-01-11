def main():
    book_name = input("What book would you like to analyze?")
    with open("books/" + book_name + ".txt") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    character_count = count_characters(file_contents)
    
    chars_list = []
    for char, count in character_count.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/" + book_name + ".txt ---")
    print(f"{total_words} words found in the document")
    print()

    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    my_dict = {}
    lower_contents = file_contents.lower()
    for character in lower_contents:
        if character.isalpha():
            if character in my_dict:
                my_dict[character] += 1
            else:
                my_dict[character] = 1
    return my_dict

def sort_on(chars_list):
    return chars_list["count"]

if __name__ == "__main__":
    main()