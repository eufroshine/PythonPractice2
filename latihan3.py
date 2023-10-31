#print hello
print("Halo ini script python")
def print_diamond(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")

        # Print stars
        for k in range(1, 2 * i):
            print("*", end="")

        print()

    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")

        # Print stars
        for k in range(1, 2 * i):
            print("*", end="")

        print()

# Input the number of rows
num_rows = int(input("Enter the number of rows: "))

# Print the diamond
print_diamond(num_rows)
