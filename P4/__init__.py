from flask import Blueprint, render_template

p4_bp = Blueprint('p4', __name__, template_folder='templates', static_folder='static')

@p4_bp.route('/p4')
def index():
    return render_template('index.html')
