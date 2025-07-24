import sys

def check_args():
    if (len(sys.argv) != 2):
        return False

def split_data(argv):
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
    associated_data = {city: state for city, state in zip(capital_cities.values(), states.keys())}
    if ",," in argv:
        sys.exit()
    res = argv.split(',')
    for el in res:
        unknown = ""
        tmp = el.split(" ")
        for x in tmp:
            if x != "":
                unknown += x + ' '
        unknown = unknown[0:len(unknown) - 1]
        formatted_unknown = unknown.title()
        if (formatted_unknown in associated_data.keys()):
            print(f"{formatted_unknown} is the capital of {associated_data[formatted_unknown]}")
        elif (formatted_unknown in associated_data.values()):
            for key, value, in associated_data.items():
                if value == formatted_unknown:
                    print(f"{key} is the capital of {value}")
        else:
            if (unknown.strip() != ""):
                print(f"{unknown} is neither a capital city nor a state")

if __name__ == "__main__":
    if check_args() == False:
        sys.exit()
    split_data(sys.argv[1])