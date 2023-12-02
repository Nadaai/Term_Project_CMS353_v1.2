from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("instructor_page.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        result = {"firstName": request.form['firstName'],
                  "lastName": request.form['lastName'],
                  "userName": request.form['userName'],
                  "email": request.form["email"],
                  "type": request.form['type']}
        print(result)

        return redirect(url_for('home'))

    return render_template('addForm.html')


@app.route('/group')
def group():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
