from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    include_digits = 'include_digits' in request.form
    include_special_chars = 'include_special_chars' in request.form

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    
    return render_template('index.html', generated_password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)
