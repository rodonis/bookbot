char_set = set()
char_count = {}


def count_words(book: str) -> int:
    count_list = book.split()
    return len(count_list)


def count_chars(book: str) -> dict:
    # Returning a dictionary of {"char":"int"}
    book = book.lower()  # We're casting the book to all lower case characters.
    for c in book:
        char_set.add(c.lower())
    for ch in char_set:
        count = 0
        for c in book:
            if c == ch:
                count += 1
        char_count[ch] = count
    return char_count
