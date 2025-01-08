def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    longest_word = find_longest(file_contents)
    character_count = count_characters(file_contents)
    print(f"Total words: {total_words}")
    print(f"Character count: {character_count}")
    print(f"Longest word: '{longest_word}' with {len(longest_word)} characters")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    my_dict = {}
    lower_contents = file_contents.lower()
    for character in lower_contents:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1
    return my_dict

def find_longest(file_contents):
    longest_word = ""
    current_longest = 0
    words = file_contents.split()
    for word in words:
        if len(word) > current_longest:
            current_longest = len(word)
            longest_word = word
    return longest_word
if __name__ == "__main__":
    main()