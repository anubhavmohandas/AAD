from flask import Blueprint, render_template

# Define the blueprint for Practical 7
p7_bp = Blueprint('p7', __name__, template_folder='templates', static_folder='static')

# Define the route for the index page of Practical 7
@p7_bp.route('/p7')  # Changed route to match the unique prefix
def p7_index():
    # Render the appropriate template
    return render_template('index.html')
