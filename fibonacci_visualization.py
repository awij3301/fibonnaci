"""
Fibonacci Sequence Visualization

This module provides visualization tools for the Fibonacci sequence using matplotlib.
It includes line plots, bar charts, spiral visualizations, and golden ratio analysis.
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
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


def plot_fibonacci_spiral_3d(count=10):
    """
    Plot the Fibonacci spiral in 3D with increasing height.
    
    Args:
        count (int): Number of Fibonacci numbers to use for the spiral
    """
    fib_numbers = fibonacci_sequence(count)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Starting position and direction
    x, y, z = 0, 0, 0
    direction = 0  # 0: right, 1: up, 2: left, 3: down
    
    colors = plt.cm.viridis(np.linspace(0, 1, count))
    
    # Store points for spiral line
    spiral_x, spiral_y, spiral_z = [], [], []
    
    for i, fib_num in enumerate(fib_numbers):
        if fib_num == 0:
            continue
            
        # Calculate the center of the current square for the spiral
        if direction == 0:  # right
            center_x = x + fib_num
            center_y = y
            next_x = x + fib_num
            next_y = y
        elif direction == 1:  # up
            center_x = x - fib_num
            center_y = y + fib_num
            next_x = x - fib_num
            next_y = y + fib_num
        elif direction == 2:  # left
            center_x = x - fib_num
            center_y = y - fib_num
            next_x = x - fib_num
            next_y = y - fib_num
        else:  # down (direction == 3)
            center_x = x
            center_y = y - fib_num
            next_x = x
            next_y = y - fib_num
        
        # Draw 3D spiral curve
        theta = np.linspace(0, np.pi/2, 50)
        if direction == 0:  # right
            spiral_x_segment = x + fib_num - fib_num * np.cos(theta)
            spiral_y_segment = y + fib_num * np.sin(theta)
        elif direction == 1:  # up
            spiral_x_segment = x - fib_num + fib_num * np.cos(theta + np.pi/2)
            spiral_y_segment = y + fib_num + fib_num * np.sin(theta + np.pi/2)
        elif direction == 2:  # left
            spiral_x_segment = x - fib_num + fib_num * np.cos(theta + np.pi)
            spiral_y_segment = y - fib_num + fib_num * np.sin(theta + np.pi)
        else:  # down
            spiral_x_segment = x + fib_num * np.cos(theta + 3*np.pi/2)
            spiral_y_segment = y - fib_num + fib_num * np.sin(theta + 3*np.pi/2)
        
        spiral_z_segment = np.full_like(spiral_x_segment, z)
        
        # Plot the spiral segment
        ax.plot(spiral_x_segment, spiral_y_segment, spiral_z_segment, 
                color=colors[i], linewidth=3, alpha=0.8)
        
        # Draw vertical lines to show the 3D structure
        if i > 0:
            ax.plot([center_x, center_x], [center_y, center_y], [z-fib_num/10, z+fib_num/10], 
                   color=colors[i], linewidth=2, alpha=0.6)
        
        # Update position for next iteration
        x, y = next_x, next_y
        z += fib_num * 0.1  # Increase height with each iteration
        direction = (direction + 1) % 4
        
        # Add text labels
        ax.text(center_x, center_y, z, str(fib_num), fontsize=10, fontweight='bold')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Fibonacci Spiral', fontsize=16)
    
    # Set equal aspect ratio
    all_x = []
    all_y = []
    
    # Recalculate the spiral points for proper axis scaling
    x, y, z = 0, 0, 0
    direction = 0
    
    for i, fib_num in enumerate(fib_numbers):
        if fib_num == 0:
            continue
            
        if direction == 0:  # right
            all_x.extend([x, x + fib_num])
            all_y.extend([y, y + fib_num])
            x += fib_num
        elif direction == 1:  # up
            all_x.extend([x - fib_num, x])
            all_y.extend([y, y + fib_num])
            y += fib_num
        elif direction == 2:  # left
            all_x.extend([x - fib_num, x])
            all_y.extend([y - fib_num, y])
            x -= fib_num
        else:  # down
            all_x.extend([x, x + fib_num])
            all_y.extend([y - fib_num, y])
            y -= fib_num
        
        direction = (direction + 1) % 4
    
    if all_x and all_y:
        x_range = max(all_x) - min(all_x)
        y_range = max(all_y) - min(all_y)
        max_range = max(x_range, y_range)
        
        center_x = (max(all_x) + min(all_x)) / 2
        center_y = (max(all_y) + min(all_y)) / 2
        
        ax.set_xlim([center_x - max_range/2, center_x + max_range/2])
        ax.set_ylim([center_y - max_range/2, center_y + max_range/2])
    
    ax.set_zlim([0, z + 1])
    
    plt.tight_layout()
    plt.show()


def plot_fibonacci_bar_chart_3d(count=12):
    """
    Plot the Fibonacci sequence as a 3D bar chart.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
    """
    fib_numbers = fibonacci_sequence(count)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create coordinates for 3D bars
    x_pos = np.arange(count)
    y_pos = np.zeros(count)
    z_pos = np.zeros(count)
    
    # Bar dimensions
    dx = np.ones(count) * 0.8
    dy = np.ones(count) * 0.8
    dz = fib_numbers
    
    # Create color map
    colors = plt.cm.viridis(np.linspace(0, 1, count))
    
    # Plot 3D bars
    for i in range(count):
        ax.bar3d(x_pos[i], y_pos[i], z_pos[i], dx[i], dy[i], dz[i], 
                color=colors[i], alpha=0.8, edgecolor='black', linewidth=1)
        
        # Add value labels on top of bars
        ax.text(x_pos[i] + dx[i]/2, y_pos[i] + dy[i]/2, dz[i] + max(fib_numbers)*0.02,
                str(fib_numbers[i]), ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Index (n)')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fibonacci Number F(n)')
    ax.set_title(f'3D Fibonacci Bar Chart (First {count} Numbers)', fontsize=16)
    
    # Set the viewing angle
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    plt.show()


def plot_golden_ratio_convergence(count=20):
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


def plot_fibonacci_surface_3d(count=20):
    """
    Plot a 3D surface showing Fibonacci growth over time and position.
    
    Args:
        count (int): Number of points to use for the surface
    """
    # Generate Fibonacci numbers
    fib_numbers = fibonacci_sequence(count)
    
    # Create a grid for the surface
    x = np.arange(count)
    y = np.arange(count)
    X, Y = np.meshgrid(x, y)
    
    # Create Z values based on Fibonacci sequence
    Z = np.zeros_like(X, dtype=float)
    for i in range(count):
        for j in range(count):
            # Create a surface that shows how Fibonacci numbers grow
            # Use min to avoid index errors
            idx = min(i + j, count - 1)
            Z[i, j] = fib_numbers[idx]
    
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create the surface plot
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                          linewidth=0, antialiased=True)
    
    # Add contour lines for better visualization
    contours = ax.contour(X, Y, Z, levels=10, colors='black', alpha=0.4, linewidths=0.5)
    
    # Add a color bar
    fig.colorbar(surf, shrink=0.5, aspect=20, pad=0.1)
    
    ax.set_xlabel('X Index')
    ax.set_ylabel('Y Index')
    ax.set_zlabel('Fibonacci Value')
    ax.set_title('3D Fibonacci Surface', fontsize=16)
    
    # Set viewing angle
    ax.view_init(elev=30, azim=45)
    
    plt.tight_layout()
    plt.show()


def plot_fibonacci_helix_3d(count=15):
    """
    Plot Fibonacci numbers as a 3D helix.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
    """
    fib_numbers = fibonacci_sequence(count)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create helix coordinates
    t = np.linspace(0, 4*np.pi, count)
    x = np.cos(t)
    y = np.sin(t)
    z = np.arange(count)
    
    # Create color map based on Fibonacci values
    colors = plt.cm.viridis(np.array(fib_numbers) / max(fib_numbers))
    
    # Plot the helix with varying point sizes based on Fibonacci values
    for i in range(count):
        ax.scatter(x[i], y[i], z[i], c=[colors[i]], s=fib_numbers[i]*5, alpha=0.7)
        
        # Add text labels
        ax.text(x[i], y[i], z[i], str(fib_numbers[i]), 
               fontsize=8, fontweight='bold')
    
    # Connect points with lines
    ax.plot(x, y, z, 'b-', linewidth=2, alpha=0.6)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Index (n)')
    ax.set_title('3D Fibonacci Helix', fontsize=16)
    
    # Set viewing angle
    ax.view_init(elev=20, azim=45)
    
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


def create_fibonacci_3d_dashboard(count=15):
    """
    Create a comprehensive 3D dashboard with multiple Fibonacci visualizations.
    
    Args:
        count (int): Number of Fibonacci numbers to use
    """
    # Create a figure with 2x2 subplots for 3D visualizations
    fig = plt.figure(figsize=(16, 12))
    
    # 1. 3D Spiral
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    fib_numbers = fibonacci_sequence(8)  # Use fewer for spiral
    
    # Simplified 3D spiral for dashboard
    x, y, z = 0, 0, 0
    direction = 0
    colors = plt.cm.viridis(np.linspace(0, 1, 8))
    
    for i, fib_num in enumerate(fib_numbers):
        if fib_num == 0:
            continue
        
        # Simple spiral calculation
        theta = np.linspace(0, np.pi/2, 20)
        if direction == 0:
            sx = x + fib_num - fib_num * np.cos(theta)
            sy = y + fib_num * np.sin(theta)
        elif direction == 1:
            sx = x - fib_num + fib_num * np.cos(theta + np.pi/2)
            sy = y + fib_num + fib_num * np.sin(theta + np.pi/2)
        elif direction == 2:
            sx = x - fib_num + fib_num * np.cos(theta + np.pi)
            sy = y - fib_num + fib_num * np.sin(theta + np.pi)
        else:
            sx = x + fib_num * np.cos(theta + 3*np.pi/2)
            sy = y - fib_num + fib_num * np.sin(theta + 3*np.pi/2)
        
        sz = np.full_like(sx, z)
        ax1.plot(sx, sy, sz, color=colors[i], linewidth=2)
        
        # Update position
        if direction == 0:
            x += fib_num
        elif direction == 1:
            y += fib_num
        elif direction == 2:
            x -= fib_num
        else:
            y -= fib_num
        
        z += fib_num * 0.1
        direction = (direction + 1) % 4
    
    ax1.set_title('3D Fibonacci Spiral', fontsize=12)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # 2. 3D Bar Chart
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    fib_numbers = fibonacci_sequence(10)  # Use fewer for dashboard
    
    x_pos = np.arange(10)
    y_pos = np.zeros(10)
    z_pos = np.zeros(10)
    dx = np.ones(10) * 0.8
    dy = np.ones(10) * 0.8
    dz = fib_numbers
    
    colors = plt.cm.viridis(np.linspace(0, 1, 10))
    
    for i in range(10):
        ax2.bar3d(x_pos[i], y_pos[i], z_pos[i], dx[i], dy[i], dz[i], 
                 color=colors[i], alpha=0.8)
    
    ax2.set_title('3D Fibonacci Bars', fontsize=12)
    ax2.set_xlabel('Index')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Value')
    
    # 3. 3D Helix
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    fib_numbers = fibonacci_sequence(12)
    
    t = np.linspace(0, 4*np.pi, 12)
    x = np.cos(t)
    y = np.sin(t)
    z = np.arange(12)
    
    colors = plt.cm.viridis(np.array(fib_numbers) / max(fib_numbers))
    
    for i in range(12):
        ax3.scatter(x[i], y[i], z[i], c=[colors[i]], s=fib_numbers[i]*3, alpha=0.7)
    
    ax3.plot(x, y, z, 'b-', linewidth=1, alpha=0.6)
    ax3.set_title('3D Fibonacci Helix', fontsize=12)
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Index')
    
    # 4. 3D Surface (simplified)
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    fib_numbers = fibonacci_sequence(15)
    
    x = np.arange(8)
    y = np.arange(8)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X, dtype=float)
    
    for i in range(8):
        for j in range(8):
            idx = min(i + j, 14)
            Z[i, j] = fib_numbers[idx]
    
    surf = ax4.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, linewidth=0)
    ax4.set_title('3D Fibonacci Surface', fontsize=12)
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Value')
    
    plt.tight_layout()
    plt.show()


def main():
    """
    Demonstrate various Fibonacci visualizations.
    """
    print("Fibonacci Sequence Visualizations\n")
    
    # Create individual 2D plots
    print("=== 2D Visualizations ===")
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
    
    print("6. Comprehensive 2D dashboard...")
    create_fibonacci_dashboard(15)
    
    print("\n=== 3D Visualizations ===")
    print("7. 3D Fibonacci spiral...")
    plot_fibonacci_spiral_3d(8)
    
    print("8. 3D Bar chart...")
    plot_fibonacci_bar_chart_3d(12)
    
    print("9. 3D Surface plot...")
    plot_fibonacci_surface_3d(15)
    
    print("10. 3D Helix...")
    plot_fibonacci_helix_3d(12)
    
    print("11. Comprehensive 3D dashboard...")
    create_fibonacci_3d_dashboard(15)


def main_3d_only():
    """
    Demonstrate only the 3D Fibonacci visualizations.
    """
    print("3D Fibonacci Sequence Visualizations\n")
    
    print("1. 3D Fibonacci spiral...")
    plot_fibonacci_spiral_3d(8)
    
    print("2. 3D Bar chart...")
    plot_fibonacci_bar_chart_3d(12)
    
    print("3. 3D Surface plot...")
    plot_fibonacci_surface_3d(15)
    
    print("4. 3D Helix...")
    plot_fibonacci_helix_3d(12)
    
    print("5. Comprehensive 3D dashboard...")
    create_fibonacci_3d_dashboard(15)


if __name__ == "__main__":
    # Run all visualizations (2D and 3D)
    main()
    
    # Uncomment the line below to run only 3D visualizations
    # main_3d_only()