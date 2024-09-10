from flask import Blueprint, render_template

p6_bp = Blueprint('p6', __name__, template_folder='templates', static_folder='static')

@p6_bp.route('/p6')
def index():
    return render_template('index.html')
