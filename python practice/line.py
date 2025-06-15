import sys

def count_file_stats(file_path):
    try:
        with open('Apple.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            character_count = len(content)
            line_count = len(lines)
            word_count = len(words)

            return line_count, word_count, character_count
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_stats.py 'file_path'")
    else:
        file_path = sys.argv[1]
        stats = count_file_stats(file_path)
        if isinstance(stats, tuple):
            line_count, word_count, character_count = stats
            print(f"Lines: {line_count}")
            print(f"Words: {word_count}")
            print(f"Characters: {character_count}")
        else:
            print(stats)
