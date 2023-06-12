from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed,FileRequired

class ReviewForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired(message="Поле не должо быть пустым")])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message="Поле не должо быть пустым")])
    score = SelectField('Оценка', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default=10)
    submit = SubmitField('Отправить')

class FilmForm(FlaskForm):
        title = StringField("Название фильма", validators=[
            DataRequired(message='Поле "Название фильма" не может быть пустым'),
            Length(max=255, message="Название не может быть более 255 символов")
        ])
        description = TextAreaField("Описание фильма", validators=[
            DataRequired(message='Поле "Описание фильма" не может быть пустым')
        ])
        image = FileField("Постер фильма", validators=[
            DataRequired(message='Поле "Постер фильма" не может быть пустым')
        ])
        submit = SubmitField("Добавить фильм")

#validators=[FileAllowed(['png','jpeg','jpg'],message="Неверный формат файла")]