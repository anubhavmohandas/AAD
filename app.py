# from flask import Flask
# from P1 import p1_bp
# from P2.practical import practical_bp
# from P2.practical2 import practical2_bp
# from P3 import p3_bp
# from P4 import p4_bp
# from P5 import p5_bp
# from P6 import p6_bp
# from P7 import p7_bp

# app = Flask(__name__)

# # Register blueprints for each practical
# app.register_blueprint(p1_bp, url_prefix='/practical1')
# app.register_blueprint(practical_bp, url_prefix='/practical2')
# app.register_blueprint(practical2_bp, url_prefix='/practical2_2')
# app.register_blueprint(p3_bp, url_prefix='/practical3')
# app.register_blueprint(p4_bp, url_prefix='/practical4')
# app.register_blueprint(p5_bp, url_prefix='/practical5')
# app.register_blueprint(p6_bp, url_prefix='/practical6')
# app.register_blueprint(p7_bp, url_prefix='/practical7')

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# Route for Practical 1
@app.route('/practical1')
def practical1():
    # Assuming 'p1_1.html' is the main template for Practical 1
    return render_template('p1_1.html')

# Route for Practical 2
@app.route('/practical2')
def practical2():
    # Assuming 'index.html' is the main template for Practical 2
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 2_2
@app.route('/practical2_2')
def practical2_2():
    # Assuming 'index.html' is the main template for Practical 2_2
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 3
@app.route('/practical3')
def practical3():
    # Assuming 'index.html' is the main template for Practical 3
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 4
@app.route('/practical4')
def practical4():
    # Assuming 'index.html' is the main template for Practical 4
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 5
@app.route('/practical5')
def practical5():
    # Assuming 'index.html' is the main template for Practical 5
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 6
@app.route('/practical6')
def practical6():
    # Assuming 'index.html' is the main template for Practical 6
    return render_template('index.html')  # Adjust this if the template name is different

# Route for Practical 7
@app.route('/practical7')
def practical7():
    # Assuming 'index.html' is the main template for Practical 7
    return render_template('index.html')  # Adjust this if the template name is different

if __name__ == "__main__":
    app.run(debug=True)
