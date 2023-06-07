def split_and_join(line):
    words = line.split(" ")  # Split the line into a list of words
    hyphenated_string = "-".join(words)  # Join the words using a hyphen
    return hyphenated_string

if __name__ == '__main__':
    input_line = input()
    result = split_and_join(input_line)
    print(result)
