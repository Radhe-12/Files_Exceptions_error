def write_and_apend():
    user_input = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')
    print("\nData successfully written to output.txt.\n")

    user_input1 = input("Enter additional text to append: ")
    with open('output.txt', 'a')as file:
        file.write(user_input1 +'\n')
    print("\nData successfully appended.\n")

    print("Final content of output.txt:\n")
    with open('output.txt', 'r')as file:
        for line in file:
            print(line.strip())

write_and_apend()
