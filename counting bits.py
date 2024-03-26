
def DecimalToBinaryCount(num):
    counter = [0]
    for i in range(1, num+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter


def main():
    ans = []
    while True:
        num = input("Enter a number between 0 and 105 (-1 to end): ")

        if num.isdigit() == False:
            print("Enter a digit")
            return

        n = int(num)

        if n == -1:
            break
        if n >= 0 and n <= 105:
            for i in range(n+1):
                res = DecimalToBinaryCount(i)
                ans.append(res)
        else:
            print("Invalid Input")
            print('\n')
            continue
        print(f'The number of One' + '\'' +
              's in binary of range of ' + str(n) + ': ', end='')
        print(ans)
        ans.clear()
        print('\n')


if __name__ == '__main__':
    main()
