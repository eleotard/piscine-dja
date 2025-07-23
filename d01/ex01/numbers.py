def ft():
    f = open("numbers.txt")
    res = f.read().split(',')
    for x in res:
        print(x)

if __name__ == '__main__':
    ft()