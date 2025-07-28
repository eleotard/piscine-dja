import sys

SOURCE_FILE = "periodic_table.txt"
CSS_FILE = "style.css"
HTML_FILE = "periodic_table.html"

def create_html_file(d):
    html_document = f"""
<!DOCTYPE html>
<html lang=en>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width-device-width initial-scale=1.0">
        <title>Periodic Table</title>
        <link rel="stylesheet" href={CSS_FILE}>
    </head>
    <body>
        <h1>PERIODIC TABLE OF ELEMENTS</h1>
        <table>
"""
    col = 0
    index = 0
    for col in range(0, 7):
        row = 0
        html_document += "\t\t\t<tr>\n"
        for r in range(0, 18):
            if index < len(d) and r == int(d[index]["pos"]):
                html_document += f"\t\t\t\t<td>\n\t\t\t\t\t<h4>{d[index]["name"]}</h4>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li>No {d[index]["num"]}</li>\n\t\t\t\t\t\t<li>{d[index]["symb"]}</li>\n\t\t\t\t\t\t<li>{d[index]["mass"]}</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</td>\n"
                index += 1
            else:
                html_document += "\t\t\t\t<td style=\"border: 0px solid #000000; padding: 5px;\"></td>\n"
    html_document += "\t\t\t</tr>\n\t\t</table>\n\t</body>\n</html>\n"
    with open(HTML_FILE, "w") as file:
        file.write(html_document)

def generate_css():
    css_document = f"""
    table {{
        margin: auto;
        border-collapse: collapse;
    }}
    th, td {{
        border: 1px solid #000000;
        padding: 5px;
        font-family: 'Arial', sans-sherif;
        padding-left: 20px;
    }}
    h1 {{
        text-align: center;
        font-family: 'Arial', sans-sherif;
    }}
    h1 {{
        text-align: center;
        font-family: 'Arial', sans-sherif;
    }}

    ul {{
        margin:0px;
        padding:0px;
        position:relative;
    }}
    """
    with open(CSS_FILE, "w") as file:
        file.write(css_document)

def create_tab_of_elements(file):
    if not file:
        sys.exit()
    a = [] 
    for line in file:
        tmp = line.split(" = ")
        if len(tmp) != 2:
            sys.exit()
        params = tmp[1][:-1]
        name = tmp[0]
        params = params.split(", ")
        if len(params) != 5:
            sys.exit()
        for i in range(0, len(params)):
            index = params[i].find(":")
            if index == -1:
                sys.exit()
            params[i] = params[i][index + 1:]
        a.append({"name": name, "pos": params[0], "num": params[1], "symb": params[2], "mass": params[3]})
    return a

if __name__ == "__main__":
    generate_css()
    try:   
        with open(SOURCE_FILE, "r") as periodic_file:
            elements = create_tab_of_elements(periodic_file)
    except:
        sys.exit()    
    create_html_file(elements)