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

    if ('predators' not in session):
        session['predators'] = 1
        print('------------ predator if statement')
    else:
        session['predators'] += 1
        print('------------ predator else statement')

    return render_template("index.html")

@app.route('/visit', methods=['POST'])
def count_visits():
    print('---------/visit route ran')
    session['visits'] = int(request.form['visits']) + session['visits'] -1
    print("--------------",type(session['visits']))
    return redirect('/')

@app.route('/predators', methods=['POST'])
def count_predators():
    print('---------/visit route ran')
    session['predators'] = int(request.form['predators']) + session['predators'] -1
    print("--------------",type(session['predators']))
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits')
    session.pop('predators')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)     

# session is a dictionary and so is request.form