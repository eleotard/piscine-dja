import sys

# def read_file(file):
#     with open(file, r) as periodic_file
SOURCE_FILE = "periodic_table.txt"
CSS_FILE = "style.css"
HTML_FILE = "periodic_table.html"

            # <div style="overflow-x:auto">
def create_html_file():
    html_document = f"""
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8">
            <title>Periodic Table</title>
            <link rel="stylesheet" href={CSS_FILE}>
        </head>
        <body>
            <h1>PERIODIC TABLE OF ELEMENTS</h1>
            <table>
    """
    col = 0
    for col in range(0, 8):
        row = 0
        html_document += "<tr>\n"
        for r in range(0, 18):
            if (col == 0):
                if ((r == 0) or (r == 17)):
                    html_document += "<td></td>\n"
                else:
                    html_document += "<td style=\"border: 0px solid #000000; padding: 50px;\"></td>\n"
            elif ((col == 1) or (col == 2)):
                if ((0 <= r <= 1) or (11 <= r <= 17)):
                    html_document += "<td></td>\n"
                else:
                    html_document += "<td style=\"border: 0px solid #000000; padding: 50px;\"></td>\n"
            else:
                    html_document += "<td></td>\n"
    html_document += "</tr>\n</table>\n</body>\n<html>\n"

     
    with open(HTML_FILE, "w") as file:
        file.write(html_document)

        # width: 100%;
        # table-layout: auto;
def generate_css():
    
    css_document = f"""
    table {{
        margin: auto;
        border-collapse: collapse;
    }}
    th, td {{
                border: 1px solid #000000;
                padding: 50px;
                text-align: middle;
                font-family: 'Arial', sans-sherif;
            }}
    h1 {{
        text-align: center;
        font-family: 'Arial', sans-sherif;
    }}
    """
    with open(CSS_FILE, "w") as file:
        file.write(css_document)

def create_dict(file):
    print(periodic_file.read())
    file.seek(0)
    if not file:
        sys.exit()
    d = {}
    for line in file:
        tmp = line.split(" = ")  
        params = tmp[1][:-1]
        nom = tmp[0]
        params = params.split(", ")
        for el in params:
            index = el.find(":")
            print(index)
            print()
            el = el[index:]
            print(el)
            print(params)
        d[nom] = {"num": params[0], "symb": params[1], "mass": params[2]}
        break
        # print(f"[{params}]")
        # print(f"[{tmp}]")
    print(d)

if __name__ == "__main__":
    #periodic_file = read_file("periodic_table.txt")
    generate_css()
    with open(SOURCE_FILE, "r") as periodic_file:
        elements = create_dict(periodic_file)
    create_html_file()
    # ft()