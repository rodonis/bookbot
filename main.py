import stats as s


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = s.count_words(book)
    print(f"{word_count} words found in the document")
    char_count = s.count_chars(book)
    print(f"{char_count}")


main()
