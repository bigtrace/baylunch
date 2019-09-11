from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectField,IntegerField
from wtforms.validators import DataRequired,Length


class OrderForm(FlaskForm):


    Dish_dropdown_list = [('Others', '...'), ('平安虾卷', '平安虾卷'), ('蒲烧鳗鱼', '蒲烧鳗鱼'),
                     ('卤猪肘', '卤猪肘'), ('红烧牛腩', '红烧牛腩'),('香肠肉燥', '香肠肉燥'), ('怀旧排骨', '怀旧排骨')
                     ,('卤味三拼', '卤味三拼'), ('黄金虾饼', '黄金虾饼'), ('咖喱鸡肉', '咖喱鸡肉'),('红烧扣肉', '红烧扣肉')]
    Preset_dish = SelectField('Select your Dish', choices=Dish_dropdown_list, default=1)
    Number_dish = IntegerField('Number',validators=[DataRequired()])

    Notes_dish = StringField('Addition notes',validators=[Length(min=0,max=20)])

    submit=SubmitField('Order')
