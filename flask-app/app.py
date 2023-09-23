from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/machine', methods=['POST', 'GET'])
def machine():
    if request.method == 'POST' and 'file' in request.files:
        f = request.files['file']
        f.save('uploaded/input.csv')
        return send_file('uploaded/input.csv', 
                         as_attachment=True, 
                         download_name='output.csv')
    else:
        print('No files or no post method')
    return render_template('machine.html')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
