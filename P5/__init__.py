from flask import Blueprint, render_template

p4_bp = Blueprint('p4', __name__, template_folder='templates', static_folder='static')

@p4_bp.route('/')
def p4_index():
    return render_template('index.html') 
