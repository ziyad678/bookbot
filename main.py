from stats import get_num_words, get_num_characters, report
import sys
def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    count = get_num_words(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    char_counts = get_num_characters(content)
    report (char_counts)

main()