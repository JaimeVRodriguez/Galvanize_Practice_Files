import argparse


def add_two_digits(a, b):

    return a + b


if __name__ == "__main__":

    print(add_two_digits(5, 5))

    parser = argparse.ArgumentParser(
        description="Add two numbers together.",
        epilog="This is the epilog"
    )

    # * Add positional arguments
    parser.add_argument("a", type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")

    # * Optional argument
    parser.add_argument("-c", "--cat", type=str, required=False,
                        help="optional: the name of your cat")

    # * Cast to explicit types, store for use
    args = parser.parse_args()

    # * Call the arguments
    print(f"a is: {args.a}")
    print(f"b is: {args.b}")

    print("add them together to get: ", end="")

    # * Function call
    print(add_two_digits(args.a, args.b))

    # * Call optional argument
    if args.cat:
        print(args.cat)
