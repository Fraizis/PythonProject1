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


def check_relation(net: tuple, first: str, second: str) -> bool | None:
    for tup in net:
        if first in tup:
            search_name = [name for name in tup if name != first][0]
            print('search_name:', search_name)
            new_net = tuple(elem for elem in net if elem != tup)
            if second == search_name:
                print(f'Matched: {second} == {search_name}')
                return True
            else:
                print(f'Not matched: {second} != {search_name}')
                result = check_relation(new_net, search_name, second)
                if result:
                    return result

    return False


net = (
    ("Ваня", "Лёша"),
    ("Лёша", "Катя"),
    ("Ваня", "Катя"),
    ("Вова", "Катя"),
    ("Лёша", "Лена"),
    ("Оля", "Петя"),
    ("Стёпа", "Оля"),
    ("Оля", "Настя"),
    ("Настя", "Дима"),
    ("Дима", "Маша")
)

if __name__ == '__main__':
    # print(check_relation(net=net, first='Ваня', second='Дима'))
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
    # app.run(debug=True)
