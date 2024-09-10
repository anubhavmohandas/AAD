from flask import Flask, render_template, request

app = Flask(__name__)

def dynamic_knapsack(n, W, weights, profits):
    # Initialize the table with zeros
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Fill the table using the dynamic programming approach
    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i-1] <= j:
                table[i][j] = max(table[i-1][j], profits[i-1] + table[i-1][j - weights[i-1]])
            else:
                table[i][j] = table[i-1][j]

    # Find the maximum profit
    max_profit = table[n][W]

    # Backtrack to find which items to include in the optimal solution
    included_items = []
    remaining_capacity = W
    for i in range(n, 0, -1):
        if table[i][remaining_capacity] != table[i-1][remaining_capacity]:  # Item i is included
            included_items.append((weights[i-1], profits[i-1]))
            remaining_capacity -= weights[i-1]

    # Return the filled table, maximum profit, and included items
    return table, max_profit, included_items

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        W = int(request.form['capacity'])
        n = int(request.form['num_items'])
        
        # Fetch profits and weights
        profits = list(map(int, request.form['profits'].split(',')))
        weights = list(map(int, request.form['weights'].split(',')))
        
        # Knapsack solution
        table, max_profit, included_items = dynamic_knapsack(n, W, weights, profits)
        
        # Render the result
        return render_template('index.html', table=table, max_profit=max_profit, profits=profits, weights=weights, included_items=included_items, W=W, n=n)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
