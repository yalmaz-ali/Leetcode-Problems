def main():
    command = input("Enter the text to convert it into goal: ")
    print(command.replace('()', 'o').replace('(al)', 'al'))


if __name__ == '__main__':
    main()
