from flask import Flask, render_template, request, jsonify
import feedparser
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def bmi_calc():
    bmi = ''
    bmi_cate = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
        bmi_cate = bmi_cate_info(weight, height)
    return render_template("bmi.html",
	                        bmi=bmi,
                            bmi_cate=bmi_cate)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


def bmi_cate_info(weight, height):
    bmi = round((weight / ((height / 100) ** 2)), 2)
    if bmi < 15:
        return_bmi = "Very severely underweight"
    elif bmi >= 15 and bmi < 16:
        return_bmi = "Severely underweight"
    elif bmi >= 16 and bmi < 18.5:
        return_bmi = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return_bmi = "Normal (healthy weight)"
    elif bmi >= 25 and bmi < 30:
        return_bmi = "Overweight"
    elif bmi >= 30 and bmi < 35:
        return_bmi = "Moderately obese"
    elif bmi >= 35 and bmi < 40:
        return_bmi = "Severely obese"
    elif bmi >= 40:
        return_bmi = "Very severely obese"
    else:
        return_bmi = "ERROR"
    
    return return_bmi
    