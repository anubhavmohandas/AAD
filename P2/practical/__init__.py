from flask import Blueprint, render_template

practical_bp = Blueprint('practical', __name__, template_folder='templates', static_folder='static')

@practical_bp.route('/')
def practical_index():
    return render_template('index.html')
