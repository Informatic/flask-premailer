import flask
import premailer
import logging

app = flask.Flask(__name__)


# This is everything you need
@app.template_filter('inline_styles')
def inline_styles(s):
    try:
        return premailer.transform(s)
    except:
        logging.exception('Premailer failed, sending non-inlined anyway')
        return s


@app.route('/')
def index():
    return flask.render_template('email/testing.html')


if __name__ == '__main__':
    app.run(debug=True)
