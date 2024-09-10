from flask import Blueprint, render_template

p1_bp = Blueprint('p1', __name__, template_folder='templates')

@p1_bp.route('/p1_1')
def p1_1():
    return render_template('p1_1.html')

@p1_bp.route('/p1_2')
def p1_2():
    return render_template('p1_2.html')
