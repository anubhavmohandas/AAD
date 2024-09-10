from flask import Blueprint, render_template

practical2_bp = Blueprint('practical2', __name__, template_folder='templates', static_folder='static')

@practical2_bp.route('/p2_2')
def p2_2():
    return render_template('index.html')
