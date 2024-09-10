# from flask import Flask, render_template, request
# import random
# import os
# import matplotlib.pyplot as plt

# # Use Agg backend for Matplotlib
# import matplotlib
# matplotlib.use('Agg')

# app = Flask(__name__)

# # Global variables to count comparisons
# bubble_count = 0
# insertion_count = 0
# selection_count = 0

# def bubble_sort(arr):
#     global bubble_count
#     bubble_count = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             bubble_count += 1
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def insertion_sort(arr):
#     global insertion_count
#     insertion_count = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             insertion_count += 1
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#         insertion_count += 1  # Count for the last comparison when the loop exits

# def selection_sort(arr):
#     global selection_count
#     selection_count = 0
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             selection_count += 1
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def generate_best_case(size):
#     return list(range(size))

# def generate_worst_case(size):
#     return list(range(size, 0, -1))

# def run_comparison(input_sizes):
#     results = []
#     for size in input_sizes:
#         best_case = generate_best_case(size)
#         worst_case = generate_worst_case(size)

#         # Best case
#         bubble_sort(best_case.copy())
#         bubble_best = bubble_count

#         insertion_sort(best_case.copy())
#         insertion_best = insertion_count

#         selection_sort(best_case.copy())
#         selection_best = selection_count

#         # Worst case
#         bubble_sort(worst_case.copy())
#         bubble_worst = bubble_count

#         insertion_sort(worst_case.copy())
#         insertion_worst = insertion_count

#         selection_sort(worst_case.copy())
#         selection_worst = selection_count

#         results.append((size, bubble_best, insertion_best, selection_best, bubble_worst, insertion_worst, selection_worst))

#     return results

# def plot_results(results):
#     sizes = [result[0] for result in results]
#     bubble_best_counts = [result[1] for result in results]
#     insertion_best_counts = [result[2] for result in results]
#     selection_best_counts = [result[3] for result in results]

#     bubble_worst_counts = [result[4] for result in results]
#     insertion_worst_counts = [result[5] for result in results]
#     selection_worst_counts = [result[6] for result in results]

#     plt.figure(figsize=(14, 7))

#     plt.subplot(1, 2, 1)
#     plt.plot(sizes, bubble_best_counts, label='Bubble Sort Best Case', marker='o')
#     plt.plot(sizes, insertion_best_counts, label='Insertion Sort Best Case', marker='o')
#     plt.plot(sizes, selection_best_counts, label='Selection Sort Best Case', marker='o')
#     plt.xlabel('List Size')
#     plt.ylabel('Comparison Count')
#     plt.title('Best Case Comparison Counts')
#     plt.legend()
#     plt.grid(True)

#     plt.subplot(1, 2, 2)
#     plt.plot(sizes, bubble_worst_counts, label='Bubble Sort Worst Case', marker='o')
#     plt.plot(sizes, insertion_worst_counts, label='Insertion Sort Worst Case', marker='o')
#     plt.plot(sizes, selection_worst_counts, label='Selection Sort Worst Case', marker='o')
#     plt.xlabel('List Size')
#     plt.ylabel('Comparison Count')
#     plt.title('Worst Case Comparison Counts')
#     plt.legend()
#     plt.grid(True)

#     plot_path = os.path.join('static', 'plot.png')
#     plt.savefig(plot_path)
#     plt.close()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         input_sizes = request.form.get("input_sizes")
#         input_sizes = list(map(int, input_sizes.split(",")))

#         results = run_comparison(input_sizes)
#         plot_results(results)
#         return render_template("index.html", results=results)
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
import random
import os
import matplotlib.pyplot as plt

# Use Agg backend for Matplotlib
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Global variables to count comparisons
merge_count = 0
insertion_count = 0
selection_count = 0

def merge_sort(arr):
    global merge_count
    merge_count = 0
    _merge_sort(arr)

def _merge_sort(arr):
    global merge_count
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        _merge_sort(L)
        _merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            merge_count += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            merge_count += 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            merge_count += 1
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    global insertion_count
    insertion_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            insertion_count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        insertion_count += 1  # Count for the last comparison when the loop exits

def selection_sort(arr):
    global selection_count
    selection_count = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            selection_count += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def generate_best_case(size):
    return list(range(size))

def generate_worst_case(size):
    return list(range(size, 0, -1))

def run_comparison(input_sizes):
    results = []
    for size in input_sizes:
        best_case = generate_best_case(size)
        worst_case = generate_worst_case(size)

        # Best case
        merge_sort(best_case.copy())
        merge_best = merge_count

        insertion_sort(best_case.copy())
        insertion_best = insertion_count

        selection_sort(best_case.copy())
        selection_best = selection_count

        # Worst case
        merge_sort(worst_case.copy())
        merge_worst = merge_count

        insertion_sort(worst_case.copy())
        insertion_worst = insertion_count

        selection_sort(worst_case.copy())
        selection_worst = selection_count

        results.append((size, merge_best, insertion_best, selection_best, merge_worst, insertion_worst, selection_worst))

    return results

def plot_results(results):
    sizes = [result[0] for result in results]
    merge_best_counts = [result[1] for result in results]
    insertion_best_counts = [result[2] for result in results]
    selection_best_counts = [result[3] for result in results]

    merge_worst_counts = [result[4] for result in results]
    insertion_worst_counts = [result[5] for result in results]
    selection_worst_counts = [result[6] for result in results]

    plt.figure(figsize=(14, 7))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, merge_best_counts, label='Merge Sort Best Case', marker='o')
    plt.plot(sizes, insertion_best_counts, label='Insertion Sort Best Case', marker='o')
    plt.plot(sizes, selection_best_counts, label='Selection Sort Best Case', marker='o')
    plt.xlabel('List Size')
    plt.ylabel('Comparison Count')
    plt.title('Best Case Comparison Counts')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(sizes, merge_worst_counts, label='Merge Sort Worst Case', marker='o')
    plt.plot(sizes, insertion_worst_counts, label='Insertion Sort Worst Case', marker='o')
    plt.plot(sizes, selection_worst_counts, label='Selection Sort Worst Case', marker='o')
    plt.xlabel('List Size')
    plt.ylabel('Comparison Count')
    plt.title('Worst Case Comparison Counts')
    plt.legend()
    plt.grid(True)

    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_sizes = request.form.get("input_sizes")
        input_sizes = list(map(int, input_sizes.split(",")))

        results = run_comparison(input_sizes)
        plot_results(results)
        return render_template("index.html", results=results)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
