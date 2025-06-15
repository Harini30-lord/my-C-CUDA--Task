import sys
from wordcount import count_words

def main():
    if len(sys.argv) != 2:
        print("Usage: command.py <filename>")
        return

    filename = sys.argv[1]
    word_counts = count_words(Apple.txt)

    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
