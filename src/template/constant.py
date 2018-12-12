HTML = '''
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="0.5">
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
            <div class="board"> {board}</div>
            <div class="blank"></div>
        </body>
    </html>
'''
HTML_CASE = '<div class="{color}">{value}</div>'
BLANK_LINE = '<div class="blank"></div>'
REPLACE_LINE = '<br><br><div class="board">{board}</div><div class="blank"></div>'
