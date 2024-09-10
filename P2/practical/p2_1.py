from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

# Use Agg backend for Matplotlib
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Initialize the count variables
count_loop = 0
count_eqn = 0
count_rec = 0

def sum_using_loop(n):
    global count_loop
    total = 0
    for i in range(1, n + 1):
        total += i
        count_loop += 1
    return total

def sum_using_equation(n):
    global count_eqn
    count_eqn += 1
    return n * (n + 1) // 2

def sum_using_recursion(n):
    global count_rec
    count_rec += 1
    if n == 1:
        count_rec += 1
        return 1
    else:
        count_rec += 1
        return n + sum_using_recursion(n - 1)

def compare_methods(inputs):
    global count_loop, count_eqn, count_rec
    results = []
    for n in inputs:
        # Reset counts for each input
        count_loop = 0
        count_eqn = 0
        count_rec = 0

        # Using loop
        sum_using_loop(n)
        loop_count = count_loop

        # Using equation
        sum_using_equation(n)
        eqn_count = count_eqn

        # Using recursion
        try:
            sum_using_recursion(n)
            rec_count = count_rec
        except RecursionError:
            rec_count = float('inf')

        results.append((n, loop_count, eqn_count, rec_count))

    return results

def plot_results(results):
    n_values = [result[0] for result in results]
    loop_counts = [result[1] for result in results]
    eqn_counts = [result[2] for result in results]
    rec_counts = [result[3] for result in results]

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, loop_counts, label='Loop Count')
    plt.plot(n_values, eqn_counts, label='Equation Count')
    plt.plot(n_values, rec_counts, label='Recursion Count')
    plt.xlabel('N')
    plt.ylabel('Count of Steps')
    plt.title('Comparison of Sum Calculation Methods by Step Count')
    plt.legend()
    plt.grid(True)
    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inputs = request.form.get("inputs")
        inputs = list(map(int, inputs.split(',')))
        results = compare_methods(inputs)
        plot_results(results)
        return render_template("index.html", results=results)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
