def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    longest_word = find_longest(file_contents)
    print(f"Total words: {total_words}")
    print(f"Longest word: '{longest_word}' with {len(longest_word)} characters")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

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