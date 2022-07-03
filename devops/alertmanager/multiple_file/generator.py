import string
import random


# debug 每秒 0.6m
# run   每秒 4m
def main():
    with open("file_1.txt", "w") as f1, open("file_2.txt", "w") as f2, open("file_3.txt", "w") as f3:
        while True:
            f1.write(f"{''.join(random.sample(string.ascii_letters, 8))}\n")
            f2.write(f"{''.join(random.sample(string.ascii_letters, 16))}\n")
            f3.write(f"{''.join(random.sample(string.ascii_letters, 32))}\n")


if __name__ == '__main__':
    main()
