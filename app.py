from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='post'>
            <label for='rot'>Rotate By:</label>
            <input type='text' name='rot' id='rot' value='0'></input>
            <textarea name='text'>{0}</textarea>
            <input type='submit' value='submit'>
        </form>
    </body>
</html>"""

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    text=request.form['text']
    encrypted = rotate_string(text, rot)
    return form.format(encrypted)


if __name__ == '__main__':
    app.run()
