import sys

def print_hello(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name_argument = sys.argv[1]
        print_hello(name_argument)
    else:
        print_hello()