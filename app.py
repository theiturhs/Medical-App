from flask import Flask, render_template

medicalApp = Flask(__name__)
medicalApp.config['TEMPLATES_AUTO_RELOAD'] = True

@medicalApp.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    medicalApp.run(debug=True)


# set FLASK_APP=App
# set FLASK_ENV=development
# flask run