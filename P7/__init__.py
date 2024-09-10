from flask import Blueprint, render_template

p7_bp = Blueprint('p7', __name__, template_folder='templates', static_folder='static')

@p7_bp.route('/app')
def app():
    return render_template('index.html')
