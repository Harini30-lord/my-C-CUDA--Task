import sys

def process_text_file(input_path, output_path):
    try:
        
        if not input_path or not output_path:
            raise ValueError("Both input and output file paths are required.")

        
        with open( input_path, 'r') as input_file:
        
            content = input_file.read()

    
            num_lines = len(content.split('\n'))

        # Attempt to write the result to the output file
        with open( output_path, 'w') as output_file:
            # Example: Writing the number of lines to the output file
            output_file.write(f"Number of lines in the input file: {num_lines}")

    except FileNotFoundError:
        print(f"Error: The input file '{input_path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when writing to '{output_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    process_text_file(input_file_path, output_file_path)
