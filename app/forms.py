from flask_wtf import FlaskForm
import wtforms as ws
from app import app
from .models import User



class UserForm(FlaskForm):
    username = ws.StringField('имя пользователя', validators=[
        ws.validators.DataRequired(), ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])
    submit = ws.SubmitField('Login')


class EmployeeForm(FlaskForm):
    fullname = ws.StringField('ФИО', validators=[ws.validators.DataRequired(), ])
    phone = ws.StringField('Номер телефона', validators=[ws.validators.DataRequired(), ])
    short_info = ws.TextAreaField('Короткая информация', validators=[ws.validators.DataRequired(), ])
    experience = ws.IntegerField('опыт работы', validators=[ws.validators.DataRequired(), ])
    preferred_position = ws.StringField('Короткая информация')
    user_id = ws.SelectField('Пользователь', choices=[])
    submit = ws.SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_choices = []
        with app.app_context():
            for user in User.query.all():
                self.user_choices.append((user.id, user.username))
        self._fields['user_id'].choices = self.user_choices


    def validate_fullname(self, field):
        names_split = field.data.split(' ')
        if len(names_split) == 1:
            raise ws.ValidationError("ФИО не может состоять из одного слова")


