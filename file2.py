def read_file():
    try:
        with open('data.txt', 'r') as file:
            print("Reading the file content")
    except FileNotFoundError:
        print("file is not foiund")
            
read_file()hello
