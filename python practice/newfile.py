import sys

def count_file_stats(filename):
    try:
        with open('Apple.txt', 'r') as file:
            content = file.read()

            
            lines = content.split('\n')
            num_lines = len(lines)

            
            words = content.split()
            num_words = len(words)

            
            num_chars = len(content)

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py filename")
    else:
        filename = sys.argv[1]
        count_file_stats(filename)
