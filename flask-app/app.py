from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/machine', methods=['POST', 'GET'])
def machine():
    data = [
        ('A'*10, 1),
        ('B'*10, 2),
        ('C'*10, 3)
    ]
    if request.method == 'POST':
        print(request.form)
    return render_template('machine.html', data=data)

@app.route('/water', methods=['POST', 'GET'])
def water():
    data = [
        ('A'*10, 1),
        ('B'*10, 2),
        ('C'*10, 3)
    ]
    if request.method == 'POST':
        print(request.form)
    return render_template('water.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)