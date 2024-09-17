def main():
    a = int(input("A: "))
    b = int(input("B: "))

    get_percentage(a, b)

def get_percentage(a, b):
    percent = (a / b) * 100 

    print(f"Answer: {percent:.2f}%")

if __name__ == '__main__':
    main()