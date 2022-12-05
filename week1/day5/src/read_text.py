def open_and_display(file_path):

    # * using with open as a context manager
    # with open(file_path) as file:

    #     print(file.read())

    # with open(file_path) as file:
    #     for line in file:
    #         print(line, " is a line...")

    with open(file_path) as file:
        for indx, line in enumerate(file):
            print(f"line {indx}: {line}", end="")


def append(file_path):

    with open(file_path, "a") as file:

        file.write("I appended this line\n")

        file.write("and another\n")

        file.write("and another\n")


def overwrite(file_path):

    with open(file_path, "w") as file:

        file.write("I overwrote everything")


if __name__ == "__main__":

    path = "../data/test.txt"

    append(path)

    open_and_display(path)

    overwrite(path)

    open_and_display(path)
