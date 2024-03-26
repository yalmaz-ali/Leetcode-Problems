
def PascalTriangle(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    elif rowIndex >= 2:
        last = [1, 1]
        for i in range(2, rowIndex+1):
            result2 = [1]
            for ii in range(1, i):
                result2.append(last[ii-1]+last[ii])
            result2.append(1)
            last = result2
    return last


def main():
    while True:
        rowIndex = input("Enter a number between 0 and 33 (-1 to end): ")

        if rowIndex.isdigit() == False:
            return

        n = int(rowIndex)

        if n == -1:
            break
        if n >= 0 and n <= 33:
            rowIth = PascalTriangle(n)
        else:
            print("Invalid Input")
            print('\n')
            continue
        print('The Pascal Triangle for row', n, 'is:')
        print(rowIth)
        print('\n')


if __name__ == '__main__':
    main()
