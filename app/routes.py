import requests
import json
from flask import render_template, request
from app import app

# When user first lands on the page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# When user clicks on the Search button, 
# the form will use this route to send a GET
# request to the Google Books API
@app.route('/result', methods=['GET'])
def searchBooks():
    try:
        user_search = request.values.get('usersearch', None)
        if not user_search:
            return render_template('index.html', error="Please enter a search term")
        else:
            r = requests.get('https://www.googleapis.com/books/v1/volumes?q='+user_search)
        # If success, return the response in JSON format to the page
        return render_template('index.html', content=json.loads(r.text))
            
    # Show error is error occurs
    except Exception as error:
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run()