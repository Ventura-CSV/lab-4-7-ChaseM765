def main():
    numbers = []
    previous = 10000

    while True:
        current = int(input('Enter Value: '))
        if current < previous:
            numbers.append(current)
            previous = current
        else:
            break

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
