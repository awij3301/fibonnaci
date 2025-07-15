# Fibonacci Sequence

Python implementations of the Fibonacci sequence with multiple approaches and **enhanced visualizations**.

## Features

### Core Fibonacci Implementations
- **Recursive approach** - Simple but inefficient O(2^n)
- **Iterative approach** - Efficient O(n) time, O(1) space
- **Generator approach** - Memory efficient for sequences
- **Memoized recursive approach** - Optimized recursive with caching
- **Sequence generation** - Generate lists of Fibonacci numbers
- **Prime checking** - Verify if a number is in the Fibonacci sequence

### Enhanced Visualizations
The visualization module has been completely redesigned with modern styling:

#### Visual Improvements
- **Modern color schemes** - Accessible, gradient-based palettes
- **Enhanced typography** - Better fonts and spacing
- **Professional styling** - Seaborn-inspired layouts
- **Interactive elements** - Hover tooltips and zoom capabilities
- **High-quality output** - 300 DPI exports for publications

#### Available Visualizations
1. **Line Plot** - Fibonacci sequence with gradient colors and scatter points
2. **Bar Chart** - Enhanced bars with shadows and value labels
3. **Fibonacci Spiral** - Golden ratio spiral with improved positioning
4. **Golden Ratio Convergence** - Shows convergence to φ with error bands
5. **Growth Comparison** - Linear and logarithmic scale comparisons
6. **Comprehensive Dashboard** - 9-panel analysis including:
   - Cumulative sums
   - Last digit patterns
   - Prime indicators
   - Ratio differences
   - Distribution analysis
7. **Animated Growth** - Frame-by-frame animation of sequence building

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Fibonacci Operations
```python
from fibonacci import fibonacci_sequence, fibonacci_iterative

# Generate first 10 Fibonacci numbers
sequence = fibonacci_sequence(10)
print(sequence)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Calculate 10th Fibonacci number
result = fibonacci_iterative(10)
print(result)  # 55
```

### Enhanced Visualizations
```python
from fibonacci_visualization import *

# Create individual visualizations
plot_fibonacci_sequence(20)
plot_fibonacci_bar_chart(15)
plot_fibonacci_spiral(8)
plot_golden_ratio_convergence(20)
plot_fibonacci_growth_comparison(15)
create_fibonacci_dashboard(15)

# Save all visualizations
save_all_visualizations(count=15, output_dir="./images/")
```

### Animation
```python
# Create animated growth visualization
create_animated_fibonacci_growth(15, "animation")

# Convert to GIF (requires ImageMagick)
# convert -delay 80 -loop 0 animation_frame_*.png animation.gif
```

## Examples

Run the main visualization script to see all enhanced features:

```bash
python fibonacci_visualization.py
```

This will:
- Generate and save high-quality PNG files
- Create animation frames
- Display interactive plots
- Show comprehensive dashboard

## Files

- `fibonacci.py` - Core Fibonacci implementations
- `fibonacci_visualization.py` - Enhanced visualization tools
- `requirements.txt` - Dependencies
- `images/` - Generated visualizations
- `README.md` - This documentation

## Dependencies

- `matplotlib >= 3.5.0` - Enhanced plotting
- `numpy >= 1.21.0` - Numerical computations

## Mathematical Background

The Fibonacci sequence is defined as:
- F(0) = 0, F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

Key properties visualized:
- **Golden Ratio (φ)**: lim(n→∞) F(n+1)/F(n) = (1+√5)/2 ≈ 1.618
- **Growth Rate**: F(n) ≈ φⁿ/√5 for large n
- **Spiral**: Quarter circles in Fibonacci rectangles create the golden spiral

## License

MIT License - See code for details.
