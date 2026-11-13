# Interactive Signal Generator & Analyzer

A Python-based implementation of fundamental Signals and Systems concepts, designed to generate, transform, visualize, and analyze continuous-time signal representations through numerical computation.

The project provides an interactive, menu-driven environment for studying standard signals, time-domain operations, signal decomposition, and fundamental signal properties using Python.

## Overview

Signals and Systems is a fundamental subject in electrical engineering and signal processing. Understanding signal behavior through mathematical expressions alone can be challenging.

This project addresses that problem by providing graphical representations and numerical analysis of commonly studied signals. Users can select different signal types, apply basic time-domain operations, and observe their corresponding waveforms and analytical properties.

## Key Features

### 1. Signal Generation
Generation and visualization of commonly used mathematical signals:

- Sine Signal
- Cosine Signal
- Square Signal
- Triangular Signal
- Ramp Signal
- Unit Step Signal
- Impulse Signal
- Exponential Signal

### 2. Signal Operations

Implementation of fundamental time-domain transformations:

- Time Shifting
- Time Scaling

### 3. Signal Decomposition

Decomposition of an input signal into its Even and Odd components using:

\[
x_e(t)=\frac{x(t)+x(-t)}{2}
\]

\[
x_o(t)=\frac{x(t)-x(-t)}{2}
\]

### 4. Signal Analysis

Calculation and observation of fundamental signal properties:

- Periodic and Aperiodic Classification
- Signal Energy
- Average Signal Power

### 5. Graphical Visualization

Matplotlib-based visualization of:

- Original Signal
- Even Component
- Odd Component
- Signal Reconstruction

All four representations are displayed together for convenient comparison.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical computation and signal generation |
| Matplotlib | Signal visualization and graph plotting |

## Project Structure

```text
Interactive-Signal-Generator/
│
├── project.py
├── README.md
├── requirements.txt
└── output_graph.png
```

## Installation and Setup

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Interactive-Signal-Generator
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Execute the Program

```bash
python project.py
```

## How to Use

1. Execute the Python program.
2. Select a signal from the displayed menu.
3. Enter the required amplitude and frequency values.
4. Choose whether to apply time shifting, time scaling, or no operation.
5. View the numerical analysis in the terminal.
6. Observe the generated signal plots.
7. Access the automatically saved graph as `output_graph.png`.

## Sample Output

The program generates a four-panel visualization containing:

1. Original Signal – Displays the generated or transformed waveform.
2. Even Signal – Shows the even component of the input signal.
3. Odd Signal – Shows the odd component of the input signal.
4. Signal Reconstruction – Compares the original signal with the sum of its even and odd components.

The generated visualization is saved in PNG format at 300 DPI for high-resolution output.

## Mathematical Concepts Implemented

The project demonstrates the following fundamental concepts:

- Standard Continuous-Time Signal Representation
- Time Shifting and Time Scaling
- Even and Odd Signal Decomposition
- Signal Energy
- Average Signal Power
- Periodic and Aperiodic Signal Classification

## Implementation Notes

- Signals are represented using discrete numerical samples over a finite time interval.
- Energy and average power are calculated numerically over the selected observation interval.
- The impulse signal is represented using a discrete approximation.
- Floating-point numerical errors are handled during even-odd decomposition.

## Learning Outcomes

This project demonstrates the practical implementation of theoretical Signals and Systems concepts through computational methods.

It provides experience in:

- Mathematical signal representation.
- Numerical computation using NumPy.
- Signal transformation and decomposition.
- Fundamental signal property analysis.
- Scientific plotting and visualization using Matplotlib.

## Future Scope

Potential improvements include:

- Fourier Transform and frequency-domain analysis.
- Convolution-based LTI system simulation.
- Additional signal transformation techniques.
- Improved numerical analysis and signal classification.

## Author

**Nasimuddin Ansari**

B.Tech – Computer Science and Engineering  
Specialization: Artificial Intelligence and Data Science

## License

This project is developed for academic and educational purposes.
