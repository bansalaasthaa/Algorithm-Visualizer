from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        selected_algorithm = request.form.get('algorithm')
        return redirect(url_for('index', algorithm=selected_algorithm))
    return render_template('form.html')

@app.route('/visualize')
def index():

    algorithm = request.args.get('algorithm', 'bubbleSort')
    if(algorithm == 'bubbleSort'):
        timeComplexity = 'O(n^2)'
    elif(algorithm == 'quickSort'):
        timeComplexity = 'O(n log n)'
    elif(algorithm == 'mergeSort'):
        timeComplexity = 'O(n log n)'
    elif(algorithm == 'insertionSort'):
        timeComplexity = 'O(n^2)'
    elif(algorithm == 'selectionSort'):
        timeComplexity = 'O(n^2)'
    elif(algorithm == 'heapSort'):
        timeComplexity = 'O(n log n)'
    elif(algorithm == 'shellSort'):
        timeComplexity = 'O(n^2)'
    elif(algorithm == 'radixSort'):
        timeComplexity = 'O(nk)'
    elif(algorithm == 'bucketSort'):
        timeComplexity = 'O(n^2)'
    elif(algorithm == 'bogoSort'):
        timeComplexity = 'O(infinite)'
    return render_template('index.html', algorithm=algorithm, timeComplexity=timeComplexity)

if __name__ == '__main__':
    app.run(debug=True)
