from flask_wtf import FlaskForm
from wtforms import StringField 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email  

class UploadForm (FlaskForm): 

    photo=FileField('Photo', validators =[FileRequired(), FileAllowed(['jpg','png','Images Only!'])] )
    description = StringField('Description', validators=[DataRequired()])    
    
    