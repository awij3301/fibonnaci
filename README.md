# fibonnaci
Python implementations of the Fibonacci sequence with multiple approaches and comprehensive 2D/3D visualizations.

## Features

### Fibonacci Implementations (fibonacci.py)
- Recursive approach
- Iterative approach 
- Generator approach
- Memoized recursive approach
- Sequence generation
- Fibonacci number validation

### Visualizations (fibonacci_visualization.py)
- **2D Visualizations:**
  - Line plots
  - Bar charts
  - Fibonacci spiral
  - Golden ratio convergence
  - Growth comparison
  - Comprehensive dashboard

- **3D Visualizations:**
  - 3D Fibonacci spiral (extending upward)
  - 3D bar charts
  - 3D surface plots
  - 3D helix representation
  - Comprehensive 3D dashboard

## Usage

### Basic Fibonacci Operations
```python
from fibonacci import fibonacci_sequence, fibonacci_iterative
print(fibonacci_sequence(10))  # First 10 Fibonacci numbers
```

### 2D Visualizations
```python
from fibonacci_visualization import plot_fibonacci_sequence, plot_fibonacci_spiral
plot_fibonacci_sequence(20)  # Line plot
plot_fibonacci_spiral(8)     # 2D spiral
```

### 3D Visualizations
```python
from fibonacci_visualization import plot_fibonacci_spiral_3d, plot_fibonacci_bar_chart_3d
plot_fibonacci_spiral_3d(8)     # 3D spiral
plot_fibonacci_bar_chart_3d(12) # 3D bars
```

### Run All Visualizations
```python
from fibonacci_visualization import main, main_3d_only
main()        # All visualizations (2D and 3D)
main_3d_only() # Only 3D visualizations
```

## Requirements
- matplotlib>=3.5.0
- numpy>=1.21.0
