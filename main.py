def main(path_to_file: str) -> None:
    with open(path_to_file) as f:
        file_contents = f.read()
        print("--- Begin report of books ---")
        print(f"{word_count(file_contents)} words found in the document")
        print()
        character_dict = character_counts(file_contents)
        characters = []
        for character in character_dict:
            characters.append({"character": character, "count": character_dict[character]})
        characters.sort(reverse=True, key=sort_on)
        for dict in characters:
            print(f"The '{dict['character']}' character was found {dict['count']} times")
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def character_counts(text):
    counts = {}
    for character in text.lower():
        if character in "abcdefghijklmnopqrstuvwxyz":
            if character in counts:
                counts[character] += 1
            else:
                counts[character] = 1
    return counts

main("books/frankenstein.txt")