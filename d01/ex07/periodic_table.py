import sys

# def read_file(file):
#     with open(file, r) as periodic_file

def create_html_file():
    html_document = f"""
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8">
            <title>Periodic Table</title>
            <style>
            table {
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000000;
                text-align: middle;
            }
        </style>
        </head>
        <body>
            <h1>Periodic Table of Elements</h1>
            <table>

            </table>

        </body>
        

    </html>
    """
    with open("periodic_table.html", "w") as file:
        file.write(html_document)



if __name__ == "__main__":
    #periodic_file = read_file("periodic_table.txt")
    with open("periodic_table.txt", "r") as periodic_file:
        print(periodic_file.read())
    # ft()