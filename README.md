Flask-Premailer
===============

This is just a simple recipe on how to integrate [Premailer](https://github.com/peterbe/premailer) with existing [Flask](http://flask.pocoo.org)
app using Jinja templates for mail styling.


Usage
-----
Just take a look at `app.py` and `templates/mail/base.html` and you will get
how it works.

*Note:* You might want to add some caching so as not to transform single email
multiple times
