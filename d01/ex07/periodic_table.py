import sys

# def read_file(file):
#     with open(file, r) as periodic_file

if __name__ == "__main__":
    #periodic_file = read_file("periodic_table.txt")
    with open("periodic_table.txt", "r") as periodic_file:
        print(periodic_file.read())
    # ft()