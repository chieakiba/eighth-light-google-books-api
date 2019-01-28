import requests
import json
from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['GET'])
def lookUpBook():
    try:
        if request.method == "GET":
            user_search = request.values.get('usersearch')
            r = requests.get('https://www.googleapis.com/books/v1/volumes?q='+user_search)
            return render_template('index.html', content=json.loads(r.text))

    except Exception as error:
        return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run()