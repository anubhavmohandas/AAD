from flask import Flask
from P1 import p1_bp
from P2.practical import practical_bp
from P2.practical2 import practical2_bp
from P3 import p3_bp
from P4 import p4_bp
from P5 import p5_bp
from P6 import p6_bp
from P7 import p7_bp

app = Flask(__name__)

# Register blueprints for each practical
app.register_blueprint(p1_bp, url_prefix='/practical1')
app.register_blueprint(practical_bp, url_prefix='/practical2_1')
app.register_blueprint(practical2_bp, url_prefix='/practical2_2')
app.register_blueprint(p3_bp, url_prefix='/practical3')
app.register_blueprint(p4_bp, url_prefix='/practical4')
app.register_blueprint(p5_bp, url_prefix='/practical5')
app.register_blueprint(p6_bp, url_prefix='/practical6')
app.register_blueprint(p7_bp, url_prefix='/practical7')

if __name__ == "__main__":
    app.run(debug=True)
