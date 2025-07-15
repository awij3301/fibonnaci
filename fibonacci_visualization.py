"""
Fibonacci Sequence Visualization

This module provides visualization tools for the Fibonacci sequence using matplotlib.
It includes line plots, bar charts, spiral visualizations, and golden ratio analysis.
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from fibonacci import fibonacci_sequence, fibonacci_iterative


def plot_fibonacci_sequence(count=20):
    """
    Plot the Fibonacci sequence as a line chart.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
    """
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    plt.figure(figsize=(12, 6))
    plt.plot(indices, fib_numbers, 'b-o', linewidth=2, markersize=6)
    plt.title(f'Fibonacci Sequence (First {count} Numbers)', fontsize=16)
    plt.xlabel('Index (n)', fontsize=12)
    plt.ylabel('Fibonacci Number F(n)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_fibonacci_bar_chart(count=15):
    """
    Plot the Fibonacci sequence as a bar chart.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
    """
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(indices, fib_numbers, color='skyblue', alpha=0.8, edgecolor='navy')
    plt.title(f'Fibonacci Sequence Bar Chart (First {count} Numbers)', fontsize=16)
    plt.xlabel('Index (n)', fontsize=12)
    plt.ylabel('Fibonacci Number F(n)', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar, value in zip(bars, fib_numbers):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(fib_numbers)*0.01,
                str(value), ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()


def plot_fibonacci_spiral(count=10):
    """
    Plot the Fibonacci spiral using squares with side lengths equal to Fibonacci numbers.
    
    Args:
        count (int): Number of Fibonacci numbers to use for the spiral
    """
    fib_numbers = fibonacci_sequence(count)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Starting position and direction
    x, y = 0, 0
    direction = 0  # 0: right, 1: up, 2: left, 3: down
    
    colors = plt.cm.viridis(np.linspace(0, 1, count))
    
    for i, fib_num in enumerate(fib_numbers):
        if fib_num == 0:
            continue
            
        # Draw square
        if direction == 0:  # right
            square = plt.Rectangle((x, y), fib_num, fib_num, 
                                 fill=False, edgecolor=colors[i], linewidth=2)
            # Draw quarter circle
            theta = np.linspace(0, np.pi/2, 100)
            circle_x = x + fib_num - fib_num * np.cos(theta)
            circle_y = y + fib_num * np.sin(theta)
            ax.plot(circle_x, circle_y, color=colors[i], linewidth=2)
            x += fib_num
        elif direction == 1:  # up
            square = plt.Rectangle((x-fib_num, y), fib_num, fib_num, 
                                 fill=False, edgecolor=colors[i], linewidth=2)
            theta = np.linspace(np.pi/2, np.pi, 100)
            circle_x = x - fib_num + fib_num * np.cos(theta)
            circle_y = y + fib_num + fib_num * np.sin(theta)
            ax.plot(circle_x, circle_y, color=colors[i], linewidth=2)
            y += fib_num
        elif direction == 2:  # left
            square = plt.Rectangle((x-fib_num, y-fib_num), fib_num, fib_num, 
                                 fill=False, edgecolor=colors[i], linewidth=2)
            theta = np.linspace(np.pi, 3*np.pi/2, 100)
            circle_x = x - fib_num + fib_num * np.cos(theta)
            circle_y = y - fib_num + fib_num * np.sin(theta)
            ax.plot(circle_x, circle_y, color=colors[i], linewidth=2)
            x -= fib_num
        else:  # down (direction == 3)
            square = plt.Rectangle((x, y-fib_num), fib_num, fib_num, 
                                 fill=False, edgecolor=colors[i], linewidth=2)
            theta = np.linspace(3*np.pi/2, 2*np.pi, 100)
            circle_x = x + fib_num * np.cos(theta)
            circle_y = y - fib_num + fib_num * np.sin(theta)
            ax.plot(circle_x, circle_y, color=colors[i], linewidth=2)
            y -= fib_num
        
        ax.add_patch(square)
        
        # Add text label
        if direction == 0:
            ax.text(x - fib_num/2, y + fib_num/2, str(fib_num), 
                   ha='center', va='center', fontsize=10, fontweight='bold')
        elif direction == 1:
            ax.text(x - fib_num/2, y - fib_num/2, str(fib_num), 
                   ha='center', va='center', fontsize=10, fontweight='bold')
        elif direction == 2:
            ax.text(x + fib_num/2, y - fib_num/2, str(fib_num), 
                   ha='center', va='center', fontsize=10, fontweight='bold')
        else:
            ax.text(x + fib_num/2, y + fib_num/2, str(fib_num), 
                   ha='center', va='center', fontsize=10, fontweight='bold')
        
        direction = (direction + 1) % 4
    
    ax.set_aspect('equal')
    ax.set_title('Fibonacci Spiral', fontsize=16)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_golden_ratio_convergence(count=20):
    """
    Plot how the ratio of consecutive Fibonacci numbers converges to the golden ratio.
    
    Args:
        count (int): Number of ratios to calculate and plot
    """
    fib_numbers = fibonacci_sequence(count + 1)
    ratios = []
    
    for i in range(1, len(fib_numbers)):
        if fib_numbers[i-1] != 0:
            ratio = fib_numbers[i] / fib_numbers[i-1]
            ratios.append(ratio)
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, len(ratios) + 1), ratios, 'b-o', linewidth=2, markersize=6, label='F(n+1)/F(n)')
    plt.axhline(y=golden_ratio, color='r', linestyle='--', linewidth=2, label=f'Golden Ratio (φ = {golden_ratio:.6f})')
    
    plt.title('Convergence to Golden Ratio', fontsize=16)
    plt.xlabel('n', fontsize=12)
    plt.ylabel('Ratio F(n+1)/F(n)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_fibonacci_growth_comparison(count=15):
    """
    Compare Fibonacci growth with exponential and polynomial functions.
    
    Args:
        count (int): Number of points to plot
    """
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    # Generate comparison functions
    exponential = [2**i for i in indices]
    polynomial = [i**2 for i in indices]
    
    plt.figure(figsize=(12, 8))
    
    # Use log scale for better comparison
    plt.semilogy(indices, fib_numbers, 'b-o', linewidth=2, markersize=6, label='Fibonacci')
    plt.semilogy(indices, exponential, 'r--', linewidth=2, label='2^n')
    plt.semilogy(indices, polynomial, 'g:', linewidth=2, label='n^2')
    
    plt.title('Fibonacci Growth Comparison (Log Scale)', fontsize=16)
    plt.xlabel('Index (n)', fontsize=12)
    plt.ylabel('Value (log scale)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def create_fibonacci_dashboard(count=15):
    """
    Create a comprehensive dashboard with multiple Fibonacci visualizations.
    
    Args:
        count (int): Number of Fibonacci numbers to use
    """
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Line plot
    ax1.plot(indices, fib_numbers, 'b-o', linewidth=2, markersize=4)
    ax1.set_title('Fibonacci Sequence', fontsize=14)
    ax1.set_xlabel('Index (n)')
    ax1.set_ylabel('Fibonacci Number')
    ax1.grid(True, alpha=0.3)
    
    # 2. Bar chart
    bars = ax2.bar(indices[:10], fib_numbers[:10], color='skyblue', alpha=0.8, edgecolor='navy')
    ax2.set_title('First 10 Fibonacci Numbers', fontsize=14)
    ax2.set_xlabel('Index (n)')
    ax2.set_ylabel('Fibonacci Number')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # 3. Golden ratio convergence
    ratios = []
    for i in range(1, len(fib_numbers)):
        if fib_numbers[i-1] != 0:
            ratio = fib_numbers[i] / fib_numbers[i-1]
            ratios.append(ratio)
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    ax3.plot(range(1, len(ratios) + 1), ratios, 'g-o', linewidth=2, markersize=4)
    ax3.axhline(y=golden_ratio, color='r', linestyle='--', linewidth=2, label=f'φ = {golden_ratio:.3f}')
    ax3.set_title('Golden Ratio Convergence', fontsize=14)
    ax3.set_xlabel('n')
    ax3.set_ylabel('F(n+1)/F(n)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Log scale comparison
    exponential = [2**i for i in indices]
    ax4.semilogy(indices, fib_numbers, 'b-o', linewidth=2, markersize=4, label='Fibonacci')
    ax4.semilogy(indices, exponential, 'r--', linewidth=2, label='2^n')
    ax4.set_title('Growth Comparison (Log Scale)', fontsize=14)
    ax4.set_xlabel('Index (n)')
    ax4.set_ylabel('Value (log scale)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def main():
    """
    Demonstrate various Fibonacci visualizations.
    """
    print("Fibonacci Sequence Visualizations\n")
    
    # Create individual plots
    print("1. Line plot of Fibonacci sequence...")
    plot_fibonacci_sequence(20)
    
    print("2. Bar chart of Fibonacci numbers...")
    plot_fibonacci_bar_chart(15)
    
    print("3. Fibonacci spiral...")
    plot_fibonacci_spiral(8)
    
    print("4. Golden ratio convergence...")
    plot_golden_ratio_convergence(20)
    
    print("5. Growth comparison...")
    plot_fibonacci_growth_comparison(15)
    
    print("6. Comprehensive dashboard...")
    create_fibonacci_dashboard(15)


if __name__ == "__main__":
    main()