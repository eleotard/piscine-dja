import sys

def check_args():
    if (len(sys.argv) != 2):
        return False

def ft(arg):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    tmp = dict([(value, key) for value in capital_cities.values(), for key in states.keys()])
    print(tmp)

    if arg in tmp:
        print(tmp[arg])
    else:
        print("Unknown capital city")

if __name__ == "__main__":
    if check_args() == False:
        sys.exit()
    ft(sys.argv[1])