from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=["POST", "GET"])

def input_str():
    if request.method == "POST":
        result = request.form['in_str']
        if len(result) == 0:
            return render_template('index.html', error='Ошибка: Поле пустое!')
        try:
            float(result)
        except:
            return render_template('index.html', error='Ошибка: Введите число!')
        else:
            session['saved_data'] = result
            return redirect(url_for('submit'))
    return render_template('index.html')

@app.route('/submit')
def submit():
    print(session['saved_data'])
    return render_template('submit.html', inp_result=session['saved_data'])

if __name__ == '__main__':
    app.run()
