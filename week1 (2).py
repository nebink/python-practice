def multiplication_table(rows, cols):
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            print(i*j, end="\t")
        print()

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    multiplication_table(rows, cols)

if __name__ == '__main__':
    main()

