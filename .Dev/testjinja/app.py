from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Add your authentication logic here (e.g., checking credentials)
    # For this example, we'll simply print the received data.
    print(f'Username: {username}, Password: {password}')

    # You can redirect the user to a different page after login, for example:
    return redirect('/dashboard')

    #return 'Login successful!'

@app.route('/dashboard', methods=['GET'])

def dashboard():
    servername = "DevServer"
    list_of_plugins = [
        {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
        {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
        {'name':'pluginname', 'author':'author', 'endpoint':'endpoint',},
        ]

    return render_template('dashboard.html', 
                           plugins=list_of_plugins,
                           servername = servername)




if __name__ == '__main__':
    app.run(debug=True)
