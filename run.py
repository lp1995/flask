from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask import Flask ,render_template,request
from sqlalchemy import *
from sqlalchemy.orm import *
app = Flask(__name__)

engin = create_engine(r'sqlite:/')

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


@app.route('/', methods=['GET', 'POST'])
def test():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('index.html', form=form)


if __name__  == '__main__':
    app.debug=True
    app.run()
