from flask import Flask, request
from flask_babel import Babel, _ 

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

babel = Babel(app, locale_selector=get_locale)

def get_locale():
    lang = request.accept_languages #.best_match(['en', 'fr'])
    return lang

@app.route('/')
def index():
    translated_text = _("Hello, World!")
    return translated_text

if __name__ == "__main__":
    app.run(debug=True)