import sys

# def read_file(file):
#     with open(file, r) as periodic_file
SOURCE_FILE = "periodic_table.txt"
CSS_FILE = "style.css"
HTML_FILE = "periodic_table.html"

            # <div style="overflow-x:auto">
def create_html_file(d):
    html_document = f"""
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport", content="width-device-width, initial-scale=1.0">
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
        html_document += "<tr>\n"
        for r in range(0, 18):
            print(index)
            if index < len(d) and r == int(d[index]["pos"]):
                html_document += f"<td><ul><h4>{d[index]["name"]}</h4></ul><li>No {d[index]["num"]}</li><li>{d[index]["symb"]}</li><li>{d[index]["mass"]}</li></td>\n"
                index += 1
            else:
                html_document += "<td style=\"border: 0px solid #000000; padding: 5px;\"></td>\n"

            
            # if (col == 0):
            #     if ((r == 0) or (r == 17)):
            #         html_document += "<td></td>\n"
            #     else:
            #         html_document += "<td style=\"border: 0px solid #000000; padding: 50px;\"></td>\n"
            # elif ((col == 1) or (col == 2)):
            #     if ((0 <= r <= 1) or (11 <= r <= 17)):
            #         html_document += "<td>{}</td>\n"
            #     else:
            #         html_document += "<td style=\"border: 0px solid #000000; padding: 50px;\"></td>\n"
            # else:
            #         html_document += "<td></td>\n"
    

    html_document += "</tr>\n</table>\n</body>\n<html>\n"

     
    with open(HTML_FILE, "w") as file:
        file.write(html_document)

        # width: 100%;
        # table-layout: auto;
                # text-align: middle;
    # li {{
    #     text-align: left;
    # }}
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
        # list-style-type:none;
    # .list li {{
    #     list-style-type: none;
    # }}
        # list-style-position: inside;
    with open(CSS_FILE, "w") as file:
        file.write(css_document)

def create_tab_of_elements(file):
    print(periodic_file.read())
    file.seek(0)
    if not file:
        sys.exit()
    a = [] 
    for line in file:
        tmp = line.split(" = ")  
        params = tmp[1][:-1]
        name = tmp[0]
        params = params.split(", ")
        for i in range(0, len(params)):
            index = params[i].find(":")
            params[i] = params[i][index + 1:]
        a.append({"name": name, "pos": params[0], "num": params[1], "symb": params[2], "mass": params[3]})
    return a

if __name__ == "__main__":
    generate_css()
    with open(SOURCE_FILE, "r") as periodic_file:
        elements = create_tab_of_elements(periodic_file)
    for el in elements:
        print(el)
    create_html_file(elements)