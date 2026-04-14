def sum(n1,n2):
    return n1+n2

def get_input():
    n1 = input('Enter the first number:')
    n2 = input('Enter the second number:')

    return n1,n2
    

def main():
    print("Hello, World!")
    n1, n2 = get_input()
    s = sum(n1,n2)
    print(f'The sum is {s}')

if __name__ == "__main__":
    main()