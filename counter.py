from flask import Flask, render_template, request, session, redirect
app = Flask (__name__)
app.secret_key = 'i am secret'


@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template('index.html', count= session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()

    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)