from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'get to the choppa'


@app.route('/')
def index():
    if ('visits' not in session):
        session['visits'] = 1
        print('------------ if statement')
    else:
        session['visits'] += 1
        print('------------ else statement')

    return render_template("index.html")

@app.route('/visit', methods=['POST'])
def count_visits():
    print('---------/visit route ran')
    session['visits'] = int(request.form['visits']) + session['visits'] -1
    print("--------------",type(session['visits']))
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True) 

# session is a dictionary and so is request.form