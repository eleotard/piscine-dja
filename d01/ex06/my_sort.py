def ft():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante' : '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    res = []
    l = [x for x in d.values()]
    l = sorted(l)
    for i in range(0, len(l)):
        tmp = []
        for key, value in d.items():
            if value == l[i]:
                tmp.append(key)
        res.append(tmp)
    for x in res:
        if len(x) > 1:
            x = sorted(x)
    print("\n".join(res))

if __name__ == "__main__":
    ft()