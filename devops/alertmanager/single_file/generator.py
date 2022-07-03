import string
import random


# debug 每秒 0.6m
# run   每秒 4m
def main():
    with open("the_file.txt", "w") as f:
        while True:
            f.write(f"{''.join(random.sample(string.ascii_letters, 32))}\n")


if __name__ == '__main__':
    main()
