from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login_page():
    # Renders login.html from the 'templates' folder
    return render_template('login.html', user_role="Seller")

if __name__ == '__main__':
    app.run(debug=True)