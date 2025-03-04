import stats as s
from sys import argv, exit


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_path = argv[1]
    book = get_book_text(book_path)
    word_count = s.count_words(book)
    print(f"Found {word_count} total words")
    char_count = s.count_chars(book)
    print(f"{char_count}")
    s.show_report()


main()
