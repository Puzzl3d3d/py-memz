import base64
import sys

def encode_file_contents(contents, times=3):
    data = contents
    for _ in range(times):
        data = base64.b64encode(data)
    return data.decode('utf-8')  # Convert bytes to string for embedding

def create_executable_output(encoded_data, output_filename='MEMZ.pyw'):
    with open(output_filename, 'w') as f:
        f.write(f'''import base64

def decode_and_execute(data, times=3):
    for _ in range(times):
        data = base64.b64decode(data)
    # Compile the decoded data
    code = compile(data, '<string>', 'exec')
    # Execute the compiled code within the global and local namespace
    exec(code, globals())

if __name__ == '__main__':
    # Encoded data
    encoded_data = {repr(encoded_data)}
    decode_and_execute(encoded_data)
''')
    print(f"Executable file '{output_filename}' has been created with encoded data.")

def main():
    #if len(sys.argv) != 2:
    #    print("Usage: python script_name.py <input_filename>")
    #    sys.exit(1)

    input_filename = "source.py"#sys.argv[1]
    try:
        with open(input_filename, 'rb') as file:
            file_contents = file.read()
        encoded_data = encode_file_contents(file_contents)
        create_executable_output(encoded_data)
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: I/O error({e.errno}): {e.strerror}")
        sys.exit(1)

if __name__ == '__main__':
    main()