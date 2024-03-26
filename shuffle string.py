def main():
    s = input("Enter the text to sort it in order of next array: ")
    indices = []
    for i in range(len(s)):
        indices.append(
            int(input("keep entering the num on which order to sort: ")))
    new_str = [None] * len(s)

    for i in range(len(s)):

        new_str[indices[i]] = s[i]

    print(''.join(new_str))


if __name__ == '__main__':
    main()
