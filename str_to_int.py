def int(str):
    NUM_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,  '6': 6, '7': 7, '8': 8, '9': 9}
    num = 0
    for i in range(len(str)):
        num = num * 10 + NUM_DICT[str[i]]
    return num


def main():
    try:
        num = input("Enter a num: ")
        print(f"number - {num} - {type(num)}")
        print(f"number - {int(num)} - {type(int(num))}")
    except Exception as ex:
        print("Not a number entered, try again...")


if __name__ == '__main__':
    main()
