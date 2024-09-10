from flask import Blueprint, render_template

p5_bp = Blueprint('p5', __name__, template_folder='templates', static_folder='static')

@p5_bp.route('/p5')
def index():
    return render_template('index.html')
