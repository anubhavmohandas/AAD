from flask import Blueprint, render_template

p3_bp = Blueprint('p3', __name__, template_folder='templates', static_folder='static')

@p3_bp.route('/app')
def index():
    return render_template('index.html')
