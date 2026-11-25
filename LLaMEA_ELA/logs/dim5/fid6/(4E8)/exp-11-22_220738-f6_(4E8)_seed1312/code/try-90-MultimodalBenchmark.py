import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial and trigonometric components
        self.poly_degree = 4
        self.wave_freq = 2.0
        self.rbf_count = min(5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**self.poly_degree)
        
        # Trigonometric wave interference pattern
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 4):
                wave_sum += np.sin(self.wave_freq * x[i] * j) * np.cos(self.wave_freq * x[i] * j)
            f_val += 0.5 * wave_sum
        
        # Adaptive radial basis functions with dynamic widths and heights
        for i in range(self.rbf_count):
            center = -4.0 + (8.0 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i * 0.7)
            height = 1.0 + 0.5 * np.cos(i * 0.9)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with sine modulation
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
            f_val += 0.3 * coupling
        
        # Asymmetric saddle points with exponential scaling
        for i in range(self.dim):
            if i % 2 == 0:
                f_val += 0.4 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.1 * x[i])
            else:
                f_val += 0.4 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.1 * x[i])
        
        # High-frequency oscillatory component with varying amplitude
        for i in range(self.dim):
            amplitude = 0.3 + 0.2 * np.sin(i * 0.5)
            f_val += amplitude * np.sin(15.0 * x[i])
            
        return f_val