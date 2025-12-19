from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def home_api():
    return render_template('form_1.html')


@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.json
    processed_data = {'message': 'Привет, ' + data['name']}
    return jsonify(processed_data)


@app.route('/form', methods=['GET'])
def home():
    return render_template('form.html')


@app.route('/greet', methods=['POST'])
def greet_form():
    username = request.form.get('username')
    surname = request.form.get('surname')
    return f'Привет {username} {surname}!'


if __name__ == '__main__':
    app.run(debug=True)
