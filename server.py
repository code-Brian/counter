from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'get to the choppa'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/visit', methods=['POST'])
def count_visits():
    print("Got Post info")
    print(request.form)
    session['visit'] = request.form['visits']
    if 'key_name' in session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
        print(request.form)
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    return render_template("destroy.html")

if __name__ == '__main__':
    app.run(debug=True) 