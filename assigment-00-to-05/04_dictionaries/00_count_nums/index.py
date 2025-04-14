def main():
    counts = {}  # Empty dictionary to store number counts

    while True:
        entry = input("Enter a number: ")
        if entry == "":
            break  # Stop input if user presses enter without typing
        number = int(entry)

        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
