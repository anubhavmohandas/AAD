from flask import Blueprint, render_template

p4_bp = Blueprint('p5', __name__, template_folder='templates', static_folder='static')

@p4_bp.route('/')
def p5_index():
    return render_template('index.html') 
