import sys

def check_args():
    if (len(sys.argv) != 2):
        return False

def associate_state_capital(arg):
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
    if arg in states:
        print(capital_cities[states[arg]])
    else:
        print("Unknown state")

if __name__ == "__main__":
    if check_args() == False:
        sys.exit()
    associate_state_capital(sys.argv[1])