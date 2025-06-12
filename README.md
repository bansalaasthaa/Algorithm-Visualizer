# Algorithm Visualizer

Algorithm Visualizer is a web application built with Flask that allows users to visualize various sorting algorithms. Users can select a sorting algorithm from a form and see the sorting process visualized with both numbers and bars, along with the name of the algorithm, its time complexity, and the number of iterations.

## Features

- Visualize different sorting algorithms
- Display algorithm name, time complexity, and number of iterations
- Interactive UI with buttons to start the sorting process
- Responsive design using Bootstrap

## Sorting Algorithms Implemented

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort
- Bucket Sort
- Shell Sort
- Bogo Sort

## Technologies Used

- Flask
- HTML
- CSS (Bootstrap)
- JavaScript

## Installation

1. Navigate to the project directory:

    ```bash
    cd AlgorithmVisualizer
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install flask
    ```

5. Run the application:

    ```bash
    flask --app app run
    ```

6. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure


- `app.py`: Main Flask application file.
- `templates/`: Folder containing HTML templates.
  - `form.html`: Template for the form to select the sorting algorithm.
  - `index.html`: Template for the sorting visualization.
- `README.md`: Project documentation.


## Usage

1. Open the form by navigating to the root URL (`/`). Select the sorting algorithm you want to visualize and click "Visualize".
2. The application will redirect to the visualization page, where you can see the sorting process.
3. Click the "Start Sorting" button to begin the visualization.



