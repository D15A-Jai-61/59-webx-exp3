from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f"You submitted: {data}"

@app.route('/get-data', methods=['GET'])
def get_data():
    return "This is a GET request response."

if __name__ == '__main__':
    app.run(debug=True)
