from flask import Blueprint, render_template

practical_bp = Blueprint('p2', __name__, template_folder='templates', static_folder='static')

@practical_bp.route('/app')
def index():
    return render_template('index.html')
