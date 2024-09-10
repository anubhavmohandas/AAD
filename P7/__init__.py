from flask import Blueprint, render_template

p7_bp = Blueprint('p7', __name__, template_folder='templates', static_folder='static')

@p7_bp.route('/')
def p7_index():
    return render_template('index.html') 
