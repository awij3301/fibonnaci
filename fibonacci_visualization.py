"""
Fibonacci Sequence Visualization

This module provides enhanced visualization tools for the Fibonacci sequence using matplotlib.
It includes modern-styled line plots, bar charts, spiral visualizations, and golden ratio analysis.
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from fibonacci import fibonacci_sequence, fibonacci_iterative
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

# Set modern matplotlib style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'sans-serif',
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 11,
    'figure.titlesize': 16,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.edgecolor': '#2E3440',
    'axes.linewidth': 1.2,
    'figure.facecolor': 'white',
    'axes.facecolor': '#F8F9FA'
})

# Define modern color palettes
FIBONACCI_COLORS = {
    'primary': '#3B82F6',      # Blue
    'secondary': '#10B981',    # Green  
    'accent': '#F59E0B',       # Amber
    'error': '#EF4444',        # Red
    'purple': '#8B5CF6',       # Purple
    'pink': '#EC4899',         # Pink
    'teal': '#14B8A6',         # Teal
    'orange': '#F97316',       # Orange
}

# Create custom colormap for gradients
colors_list = ['#3B82F6', '#10B981', '#F59E0B', '#EC4899', '#8B5CF6']
fibonacci_cmap = LinearSegmentedColormap.from_list('fibonacci', colors_list, N=256)


def plot_fibonacci_sequence(count=20, save_path=None):
    """
    Plot the Fibonacci sequence as a modern line chart with enhanced styling.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
        save_path (str): Optional path to save the plot
    """
    if count <= 0:
        raise ValueError("Count must be positive")
    
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Create gradient effect
    for i in range(1, len(indices)):
        alpha = 0.3 + 0.7 * (i / len(indices))
        ax.plot(indices[i-1:i+1], fib_numbers[i-1:i+1], 
                color=FIBONACCI_COLORS['primary'], 
                linewidth=3, alpha=alpha)
    
    # Add points with enhanced styling
    scatter = ax.scatter(indices, fib_numbers, 
                        c=indices, cmap=fibonacci_cmap, 
                        s=80, alpha=0.8, edgecolors='white', 
                        linewidth=2, zorder=5)
    
    # Enhanced styling
    ax.set_title(f'Fibonacci Sequence - First {count} Numbers', 
                fontsize=18, fontweight='bold', pad=20,
                color='#2D3748')
    ax.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
    ax.set_ylabel('Fibonacci Number F(n)', fontsize=14, fontweight='semibold')
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8, aspect=20)
    cbar.set_label('Position', fontsize=12, fontweight='semibold')
    
    # Enhanced grid
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # Add subtle background gradient
    ax.set_facecolor('#FAFAFA')
    
    # Improve layout
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    return fig


def plot_fibonacci_bar_chart(count=15, save_path=None):
    """
    Plot the Fibonacci sequence as a modern bar chart with enhanced styling.
    
    Args:
        count (int): Number of Fibonacci numbers to plot
        save_path (str): Optional path to save the plot
    """
    if count <= 0:
        raise ValueError("Count must be positive")
    
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Create gradient colors for bars
    colors = [fibonacci_cmap(i / len(indices)) for i in range(len(indices))]
    
    # Create bars with enhanced styling
    bars = ax.bar(indices, fib_numbers, color=colors, alpha=0.8, 
                 edgecolor='white', linewidth=1.5, 
                 capstyle='round')
    
    # Add gradient effect to bars
    for bar, color in zip(bars, colors):
        height = bar.get_height()
        # Add subtle shadow effect
        shadow = patches.Rectangle((bar.get_x() + 0.02, -height * 0.02), 
                                 bar.get_width(), height,
                                 facecolor='gray', alpha=0.2, zorder=0)
        ax.add_patch(shadow)
    
    # Enhanced title and labels
    ax.set_title(f'Fibonacci Sequence - First {count} Numbers', 
                fontsize=18, fontweight='bold', pad=20,
                color='#2D3748')
    ax.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
    ax.set_ylabel('Fibonacci Number F(n)', fontsize=14, fontweight='semibold')
    
    # Add value labels on bars with better positioning
    for i, (bar, value) in enumerate(zip(bars, fib_numbers)):
        height = bar.get_height()
        label_y = height + max(fib_numbers) * 0.02
        
        # Use different colors for labels based on bar height
        label_color = '#2D3748' if height < max(fib_numbers) * 0.7 else '#FFFFFF'
        
        ax.text(bar.get_x() + bar.get_width()/2, label_y,
                f'{value}', ha='center', va='bottom', 
                fontsize=10, fontweight='bold', 
                color=label_color,
                bbox=dict(boxstyle='round,pad=0.3', 
                         facecolor='white', alpha=0.8, edgecolor='none'))
    
    # Enhanced grid
    ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # Set background
    ax.set_facecolor('#FAFAFA')
    
    # Improve layout
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    return fig


def plot_fibonacci_spiral(count=10, save_path=None):
    """
    Plot the Fibonacci spiral with enhanced styling and better positioning.
    
    Args:
        count (int): Number of Fibonacci numbers to use for the spiral
        save_path (str): Optional path to save the plot
    """
    if count <= 0:
        raise ValueError("Count must be positive")
    
    fib_numbers = fibonacci_sequence(count)
    
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # Starting position and direction
    x, y = 0, 0
    direction = 0  # 0: right, 1: up, 2: left, 3: down
    
    # Enhanced color scheme
    colors = [fibonacci_cmap(i / len(fib_numbers)) for i in range(len(fib_numbers))]
    
    # Track bounds for better axis setting
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    
    for i, fib_num in enumerate(fib_numbers):
        if fib_num == 0:
            continue
        
        # Calculate square position based on direction
        if direction == 0:  # right
            square_x, square_y = x, y
            circle_center_x, circle_center_y = x + fib_num, y
            theta_start, theta_end = 0, np.pi/2
            next_x, next_y = x + fib_num, y
        elif direction == 1:  # up
            square_x, square_y = x - fib_num, y
            circle_center_x, circle_center_y = x - fib_num, y + fib_num
            theta_start, theta_end = np.pi/2, np.pi
            next_x, next_y = x, y + fib_num
        elif direction == 2:  # left
            square_x, square_y = x - fib_num, y - fib_num
            circle_center_x, circle_center_y = x - fib_num, y - fib_num
            theta_start, theta_end = np.pi, 3*np.pi/2
            next_x, next_y = x - fib_num, y
        else:  # down (direction == 3)
            square_x, square_y = x, y - fib_num
            circle_center_x, circle_center_y = x, y - fib_num
            theta_start, theta_end = 3*np.pi/2, 2*np.pi
            next_x, next_y = x, y - fib_num
        
        # Draw square with enhanced styling
        square = patches.Rectangle((square_x, square_y), fib_num, fib_num,
                                 linewidth=2.5, edgecolor=colors[i], 
                                 facecolor=colors[i], alpha=0.3)
        ax.add_patch(square)
        
        # Draw quarter circle with enhanced styling
        theta = np.linspace(theta_start, theta_end, 100)
        circle_x = circle_center_x + fib_num * np.cos(theta)
        circle_y = circle_center_y + fib_num * np.sin(theta)
        ax.plot(circle_x, circle_y, color=colors[i], linewidth=3, alpha=0.9)
        
        # Add text label with better positioning and styling
        label_x = square_x + fib_num/2
        label_y = square_y + fib_num/2
        
        # Choose text color based on background
        text_color = '#FFFFFF' if i % 2 == 0 else '#2D3748'
        
        ax.text(label_x, label_y, str(fib_num), 
               ha='center', va='center', 
               fontsize=max(8, min(14, fib_num/2)), 
               fontweight='bold', color=text_color,
               bbox=dict(boxstyle='circle,pad=0.3', 
                        facecolor='white', alpha=0.8, 
                        edgecolor=colors[i], linewidth=2))
        
        # Update bounds
        min_x = min(min_x, square_x)
        max_x = max(max_x, square_x + fib_num)
        min_y = min(min_y, square_y)
        max_y = max(max_y, square_y + fib_num)
        
        # Update position for next iteration
        x, y = next_x, next_y
        direction = (direction + 1) % 4
    
    # Enhanced styling
    ax.set_aspect('equal')
    ax.set_title('Fibonacci Spiral - Golden Ratio Visualization', 
                fontsize=18, fontweight='bold', pad=20,
                color='#2D3748')
    
    # Set axis limits with padding
    padding = max(max_x - min_x, max_y - min_y) * 0.1
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(min_y - padding, max_y + padding)
    
    # Enhanced grid
    ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_facecolor('#FAFAFA')
    
    # Add golden ratio information
    golden_ratio = (1 + math.sqrt(5)) / 2
    ax.text(0.02, 0.98, f'φ (Golden Ratio) ≈ {golden_ratio:.6f}', 
            transform=ax.transAxes, fontsize=12, 
            verticalalignment='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor='white', alpha=0.9, 
                     edgecolor=FIBONACCI_COLORS['primary']))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    return fig


def plot_golden_ratio_convergence(count=20, save_path=None):
    """
    Plot how the ratio of consecutive Fibonacci numbers converges to the golden ratio.
    
    Args:
        count (int): Number of ratios to calculate and plot
        save_path (str): Optional path to save the plot
    """
    if count <= 1:
        raise ValueError("Count must be greater than 1")
    
    fib_numbers = fibonacci_sequence(count + 1)
    ratios = []
    
    for i in range(1, len(fib_numbers)):
        if fib_numbers[i-1] != 0:
            ratio = fib_numbers[i] / fib_numbers[i-1]
            ratios.append(ratio)
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot ratios with gradient effect
    x_values = range(1, len(ratios) + 1)
    colors = [fibonacci_cmap(i / len(ratios)) for i in range(len(ratios))]
    
    # Create line plot with varying colors
    for i in range(1, len(x_values)):
        ax.plot(x_values[i-1:i+1], ratios[i-1:i+1], 
                color=colors[i], linewidth=3, alpha=0.8)
    
    # Add scatter points
    scatter = ax.scatter(x_values, ratios, c=colors, s=80, 
                        edgecolors='white', linewidth=2, zorder=5)
    
    # Golden ratio line with enhanced styling
    ax.axhline(y=golden_ratio, color=FIBONACCI_COLORS['error'], 
               linestyle='--', linewidth=3, alpha=0.8,
               label=f'Golden Ratio (φ = {golden_ratio:.6f})')
    
    # Add convergence zone
    tolerance = 0.01
    ax.fill_between(x_values, golden_ratio - tolerance, golden_ratio + tolerance,
                    alpha=0.2, color=FIBONACCI_COLORS['error'],
                    label=f'Convergence Zone (±{tolerance})')
    
    # Enhanced styling
    ax.set_title('Convergence to Golden Ratio', 
                fontsize=18, fontweight='bold', pad=20,
                color='#2D3748')
    ax.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
    ax.set_ylabel('Ratio F(n+1)/F(n)', fontsize=14, fontweight='semibold')
    
    # Enhanced legend
    ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True,
              framealpha=0.9, fontsize=12)
    
    # Enhanced grid
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_facecolor('#FAFAFA')
    
    # Add convergence information
    if len(ratios) > 10:
        final_ratio = ratios[-1]
        error = abs(final_ratio - golden_ratio)
        ax.text(0.02, 0.98, f'Final ratio: {final_ratio:.6f}\nError: {error:.6f}', 
                transform=ax.transAxes, fontsize=11, 
                verticalalignment='top', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', 
                         facecolor='white', alpha=0.9, 
                         edgecolor=FIBONACCI_COLORS['primary']))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    return fig


def plot_fibonacci_growth_comparison(count=15, save_path=None):
    """
    Compare Fibonacci growth with exponential and polynomial functions.
    
    Args:
        count (int): Number of points to plot
        save_path (str): Optional path to save the plot
    """
    if count <= 0:
        raise ValueError("Count must be positive")
    
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    # Generate comparison functions
    exponential = [2**i for i in indices]
    polynomial = [i**2 for i in indices]
    linear = [i for i in indices]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Linear scale plot
    ax1.plot(indices, fib_numbers, 'o-', linewidth=3, markersize=8, 
             color=FIBONACCI_COLORS['primary'], label='Fibonacci', alpha=0.9)
    ax1.plot(indices, exponential, 's--', linewidth=2, markersize=6, 
             color=FIBONACCI_COLORS['error'], label='2^n', alpha=0.8)
    ax1.plot(indices, polynomial, '^:', linewidth=2, markersize=6, 
             color=FIBONACCI_COLORS['secondary'], label='n²', alpha=0.8)
    ax1.plot(indices, linear, 'v-.', linewidth=2, markersize=6, 
             color=FIBONACCI_COLORS['accent'], label='n', alpha=0.8)
    
    ax1.set_title('Growth Comparison (Linear Scale)', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
    ax1.set_ylabel('Value', fontsize=14, fontweight='semibold')
    ax1.legend(frameon=True, fancybox=True, shadow=True, fontsize=12)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax1.set_facecolor('#FAFAFA')
    
    # Log scale plot
    ax2.semilogy(indices, fib_numbers, 'o-', linewidth=3, markersize=8, 
                color=FIBONACCI_COLORS['primary'], label='Fibonacci', alpha=0.9)
    ax2.semilogy(indices, exponential, 's--', linewidth=2, markersize=6, 
                color=FIBONACCI_COLORS['error'], label='2^n', alpha=0.8)
    ax2.semilogy(indices, polynomial, '^:', linewidth=2, markersize=6, 
                color=FIBONACCI_COLORS['secondary'], label='n²', alpha=0.8)
    ax2.semilogy(indices, linear, 'v-.', linewidth=2, markersize=6, 
                color=FIBONACCI_COLORS['accent'], label='n', alpha=0.8)
    
    ax2.set_title('Growth Comparison (Log Scale)', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
    ax2.set_ylabel('Value (log scale)', fontsize=14, fontweight='semibold')
    ax2.legend(frameon=True, fancybox=True, shadow=True, fontsize=12)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax2.set_facecolor('#FAFAFA')
    
    # Add growth rate information
    golden_ratio = (1 + math.sqrt(5)) / 2
    ax2.text(0.02, 0.98, f'Fibonacci ≈ φ^n where φ = {golden_ratio:.3f}', 
             transform=ax2.transAxes, fontsize=11, 
             verticalalignment='top', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', 
                      facecolor='white', alpha=0.9, 
                      edgecolor=FIBONACCI_COLORS['primary']))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Plot saved to: {save_path}")
    
    plt.show()
    return fig


def create_fibonacci_dashboard(count=15, save_path=None):
    """
    Create a comprehensive dashboard with multiple enhanced Fibonacci visualizations.
    
    Args:
        count (int): Number of Fibonacci numbers to use
        save_path (str): Optional path to save the plot
    """
    if count <= 1:
        raise ValueError("Count must be greater than 1")
    
    fib_numbers = fibonacci_sequence(count)
    indices = list(range(count))
    
    # Create subplots with better layout
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Line plot (top left)
    ax1 = fig.add_subplot(gs[0, 0])
    colors = [fibonacci_cmap(i / len(indices)) for i in range(len(indices))]
    ax1.plot(indices, fib_numbers, linewidth=3, color=FIBONACCI_COLORS['primary'], alpha=0.8)
    ax1.scatter(indices, fib_numbers, c=colors, s=60, edgecolors='white', linewidth=1.5, zorder=5)
    ax1.set_title('Fibonacci Sequence', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Position (n)', fontsize=12)
    ax1.set_ylabel('F(n)', fontsize=12)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_facecolor('#FAFAFA')
    
    # 2. Bar chart (top middle)
    ax2 = fig.add_subplot(gs[0, 1])
    bars = ax2.bar(indices[:min(10, len(indices))], fib_numbers[:min(10, len(indices))], 
                   color=colors[:min(10, len(colors))], alpha=0.8, edgecolor='white', linewidth=1.5)
    ax2.set_title('First 10 Numbers', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Position (n)', fontsize=12)
    ax2.set_ylabel('F(n)', fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax2.set_facecolor('#FAFAFA')
    
    # 3. Golden ratio convergence (top right)
    ax3 = fig.add_subplot(gs[0, 2])
    ratios = []
    for i in range(1, len(fib_numbers)):
        if fib_numbers[i-1] != 0:
            ratio = fib_numbers[i] / fib_numbers[i-1]
            ratios.append(ratio)
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    x_ratios = range(1, len(ratios) + 1)
    ax3.plot(x_ratios, ratios, 'o-', linewidth=2, markersize=6, 
             color=FIBONACCI_COLORS['secondary'], alpha=0.8)
    ax3.axhline(y=golden_ratio, color=FIBONACCI_COLORS['error'], 
                linestyle='--', linewidth=2, label=f'φ = {golden_ratio:.3f}')
    ax3.set_title('Golden Ratio Convergence', fontsize=14, fontweight='bold')
    ax3.set_xlabel('n', fontsize=12)
    ax3.set_ylabel('F(n+1)/F(n)', fontsize=12)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.set_facecolor('#FAFAFA')
    
    # 4. Growth comparison (middle left)
    ax4 = fig.add_subplot(gs[1, 0])
    exponential = [2**i for i in indices]
    ax4.semilogy(indices, fib_numbers, 'o-', linewidth=2, markersize=6, 
                color=FIBONACCI_COLORS['primary'], label='Fibonacci', alpha=0.9)
    ax4.semilogy(indices, exponential, 's--', linewidth=2, markersize=4, 
                color=FIBONACCI_COLORS['error'], label='2^n', alpha=0.8)
    ax4.set_title('Growth Comparison', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Position (n)', fontsize=12)
    ax4.set_ylabel('Value (log)', fontsize=12)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3, linestyle='--')
    ax4.set_facecolor('#FAFAFA')
    
    # 5. Ratio differences (middle middle)
    ax5 = fig.add_subplot(gs[1, 1])
    if len(ratios) > 1:
        ratio_diffs = [abs(ratio - golden_ratio) for ratio in ratios]
        ax5.semilogy(x_ratios, ratio_diffs, 'o-', linewidth=2, markersize=6, 
                    color=FIBONACCI_COLORS['purple'], alpha=0.8)
        ax5.set_title('Convergence Error', fontsize=14, fontweight='bold')
        ax5.set_xlabel('n', fontsize=12)
        ax5.set_ylabel('|F(n+1)/F(n) - φ|', fontsize=12)
        ax5.grid(True, alpha=0.3, linestyle='--')
        ax5.set_facecolor('#FAFAFA')
    
    # 6. Fibonacci percentages (middle right)
    ax6 = fig.add_subplot(gs[1, 2])
    if len(fib_numbers) > 5:
        recent_fibs = fib_numbers[-5:]
        recent_labels = [f'F({len(fib_numbers)-5+i})' for i in range(5)]
        colors_pie = [fibonacci_cmap(i / 5) for i in range(5)]
        wedges, texts, autotexts = ax6.pie(recent_fibs, labels=recent_labels, 
                                          colors=colors_pie, autopct='%1.1f%%', 
                                          startangle=90, textprops={'fontsize': 10})
        ax6.set_title('Last 5 Numbers Distribution', fontsize=14, fontweight='bold')
    
    # 7. Cumulative sum (bottom left)
    ax7 = fig.add_subplot(gs[2, 0])
    cumulative = np.cumsum(fib_numbers)
    ax7.fill_between(indices, cumulative, alpha=0.3, color=FIBONACCI_COLORS['teal'])
    ax7.plot(indices, cumulative, 'o-', linewidth=2, markersize=6, 
             color=FIBONACCI_COLORS['teal'], alpha=0.9)
    ax7.set_title('Cumulative Sum', fontsize=14, fontweight='bold')
    ax7.set_xlabel('Position (n)', fontsize=12)
    ax7.set_ylabel('Cumulative F(n)', fontsize=12)
    ax7.grid(True, alpha=0.3, linestyle='--')
    ax7.set_facecolor('#FAFAFA')
    
    # 8. Fibonacci modulo pattern (bottom middle)
    ax8 = fig.add_subplot(gs[2, 1])
    mod_values = [fib % 10 for fib in fib_numbers]
    ax8.scatter(indices, mod_values, c=colors, s=80, alpha=0.8, edgecolors='white', linewidth=1.5)
    ax8.set_title('Last Digit Pattern', fontsize=14, fontweight='bold')
    ax8.set_xlabel('Position (n)', fontsize=12)
    ax8.set_ylabel('F(n) mod 10', fontsize=12)
    ax8.set_ylim(-0.5, 9.5)
    ax8.grid(True, alpha=0.3, linestyle='--')
    ax8.set_facecolor('#FAFAFA')
    
    # 9. Prime indicators (bottom right)
    ax9 = fig.add_subplot(gs[2, 2])
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_indicators = [1 if is_prime(fib) else 0 for fib in fib_numbers]
    prime_colors = [FIBONACCI_COLORS['secondary'] if prime else FIBONACCI_COLORS['error'] 
                   for prime in prime_indicators]
    ax9.bar(indices, prime_indicators, color=prime_colors, alpha=0.8, edgecolor='white', linewidth=1.5)
    ax9.set_title('Prime Fibonacci Numbers', fontsize=14, fontweight='bold')
    ax9.set_xlabel('Position (n)', fontsize=12)
    ax9.set_ylabel('Is Prime', fontsize=12)
    ax9.set_ylim(0, 1.2)
    ax9.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax9.set_facecolor('#FAFAFA')
    
    # Overall title
    fig.suptitle('Fibonacci Sequence - Comprehensive Analysis Dashboard', 
                fontsize=20, fontweight='bold', y=0.98, color='#2D3748')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"Dashboard saved to: {save_path}")
    
    plt.show()
    return fig


def create_animated_fibonacci_growth(count=20, save_path=None):
    """
    Create an animated visualization of Fibonacci growth (saves multiple frames).
    
    Args:
        count (int): Number of Fibonacci numbers to animate
        save_path (str): Optional base path to save animation frames
    """
    if count <= 2:
        raise ValueError("Count must be greater than 2")
    
    fib_numbers = fibonacci_sequence(count)
    frames = []
    
    for frame in range(3, count + 1):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        current_fibs = fib_numbers[:frame]
        current_indices = list(range(frame))
        
        # Create gradient colors
        colors = [fibonacci_cmap(i / frame) for i in range(frame)]
        
        # Plot current sequence
        ax.plot(current_indices, current_fibs, 'o-', linewidth=3, 
                markersize=8, color=FIBONACCI_COLORS['primary'], alpha=0.8)
        
        # Highlight the newest point
        if frame > 1:
            ax.scatter([frame-1], [current_fibs[-1]], 
                      s=200, color=FIBONACCI_COLORS['error'], 
                      alpha=0.9, edgecolors='white', linewidth=3, zorder=6)
        
        # Add value labels
        for i, (x, y) in enumerate(zip(current_indices, current_fibs)):
            ax.annotate(f'{y}', (x, y), textcoords="offset points", 
                       xytext=(0,10), ha='center', fontsize=10, 
                       fontweight='bold', color='#2D3748')
        
        ax.set_title(f'Fibonacci Growth Animation - Step {frame}/{count}', 
                    fontsize=16, fontweight='bold', color='#2D3748')
        ax.set_xlabel('Position (n)', fontsize=14, fontweight='semibold')
        ax.set_ylabel('Fibonacci Number F(n)', fontsize=14, fontweight='semibold')
        
        # Set consistent axis limits
        ax.set_xlim(-0.5, count - 0.5)
        ax.set_ylim(-max(fib_numbers) * 0.1, max(fib_numbers) * 1.1)
        
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
        ax.set_facecolor('#FAFAFA')
        
        plt.tight_layout()
        
        if save_path:
            frame_path = f"{save_path}_frame_{frame:03d}.png"
            plt.savefig(frame_path, dpi=200, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            frames.append(frame_path)
        
        plt.close()  # Close to save memory
    
    if save_path:
        print(f"Animation frames saved: {len(frames)} frames")
        print(f"To create GIF, you can use: convert {save_path}_frame_*.png {save_path}.gif")
    
    return frames


def save_all_visualizations(count=15, output_dir="./images/"):
    """
    Generate and save all visualizations to files.
    
    Args:
        count (int): Number of Fibonacci numbers to use
        output_dir (str): Directory to save the visualizations
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating enhanced Fibonacci visualizations...")
    
    # Generate all visualizations
    print("1. Creating line plot...")
    plot_fibonacci_sequence(count, f"{output_dir}fibonacci_line_enhanced.png")
    
    print("2. Creating bar chart...")
    plot_fibonacci_bar_chart(count, f"{output_dir}fibonacci_bar_enhanced.png")
    
    print("3. Creating spiral visualization...")
    plot_fibonacci_spiral(min(count, 10), f"{output_dir}fibonacci_spiral_enhanced.png")
    
    print("4. Creating golden ratio convergence...")
    plot_golden_ratio_convergence(count, f"{output_dir}golden_ratio_enhanced.png")
    
    print("5. Creating growth comparison...")
    plot_fibonacci_growth_comparison(count, f"{output_dir}fibonacci_growth_enhanced.png")
    
    print("6. Creating comprehensive dashboard...")
    create_fibonacci_dashboard(count, f"{output_dir}fibonacci_dashboard_enhanced.png")
    
    print("7. Creating animation frames...")
    create_animated_fibonacci_growth(min(count, 15), f"{output_dir}fibonacci_animation")
    
    print(f"\nAll visualizations saved to: {output_dir}")


def main():
    """
    Demonstrate enhanced Fibonacci visualizations with modern styling.
    """
    print("Enhanced Fibonacci Sequence Visualizations")
    print("=" * 50)
    
    try:
        # Save all visualizations
        save_all_visualizations(count=15)
        
        print("\nDisplaying interactive visualizations...")
        
        # Create individual plots with enhanced styling
        print("\n1. Enhanced line plot of Fibonacci sequence...")
        plot_fibonacci_sequence(20)
        
        print("2. Enhanced bar chart of Fibonacci numbers...")
        plot_fibonacci_bar_chart(15)
        
        print("3. Enhanced Fibonacci spiral...")
        plot_fibonacci_spiral(8)
        
        print("4. Enhanced golden ratio convergence...")
        plot_golden_ratio_convergence(20)
        
        print("5. Enhanced growth comparison...")
        plot_fibonacci_growth_comparison(15)
        
        print("6. Enhanced comprehensive dashboard...")
        create_fibonacci_dashboard(15)
        
        print("\n" + "=" * 50)
        print("All enhanced visualizations completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your input parameters and try again.")


if __name__ == "__main__":
    main()