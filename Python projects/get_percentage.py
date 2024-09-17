def main():
    first = int(input("First: "))
    second = int(input("Second: "))

    get_percentage(first, second)

def get_percentage(a, b):
    percent = (a / b) * 100 

    print(f"Answer: {percent:.2f}%")

if __name__ == '__main__':
    main()