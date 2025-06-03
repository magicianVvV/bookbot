import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        book_text = f.read()
        return(book_text)

def get_word_count():
    book_text = get_book_text()
    words = book_text.split()
    word_count = len(words)
    print (f"Found {word_count} total words")

def get_character_count():
    character_count = {}
    book_text = get_book_text().lower()
    for chars in book_text:
        if f"{chars}" in character_count:
            character_count[f"{chars}"] += 1
        else:
            character_count[f"{chars}"] = 1
    return(character_count)
def sorted_count():
    def sort_on(dict):
        return dict["num"]
    sorted_chars = []
    character_count = get_character_count()
    for chars in character_count:
        if chars.isalpha():
            chars = {
            "char": chars,
            "num": character_count[chars]
}
            sorted_chars.append(chars)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
