# Name - Shriya Sreejith
# Assignment - HW7 - Spelling

import string

def clean_word(text):
    # remove punctuation only at beginning or end
    return text.strip(string.punctuation)

def load_dictionary(path):
    words = set()
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            term = line.strip().lower()
            if term != "":
                words.add(term)
    return words

def process_file(input_file, dictionary_file):
    dictionary = load_dictionary(dictionary_file)
    wrong_words = []
    correct_words = {}

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            for part in parts:
                cleaned = clean_word(part)
                if cleaned == "":
                    continue

                cleaned_lower = cleaned.lower()

                if cleaned_lower in dictionary:
                    if cleaned_lower not in correct_words:
                        correct_words[cleaned_lower] = 0
                    correct_words[cleaned_lower] += 1
                else:
                    wrong_words.append(cleaned_lower)


    # write misspelled words
    with open("misspelled_words.txt", "w", encoding="utf-8") as out1:
        for w in wrong_words:
            out1.write(w + "\n")

    # write correct words + counts (alphabetical)
    with open("correct_words.txt", "w", encoding="utf-8") as out2:
        for w in sorted(correct_words.keys()):
            out2.write(f"{w} {correct_words[w]}\n")

    print("The following words are not spelled correctly:")
    for w in wrong_words:
        print(w)


def main():
    user_file = input("Enter file name: ").strip()
    process_file(user_file, "words.txt")


if __name__ == "__main__":
    main()
