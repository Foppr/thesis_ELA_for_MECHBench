import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.wave_freq = 3.0
        self.rbf_count = min(7, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with modified coefficients
        f_val = 0.8 * np.sum(x**self.poly_degree)
        
        # Enhanced trigonometric wave interference with varying frequencies
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 5):
                wave_sum += np.sin(self.wave_freq * x[i] * j) * np.cos(self.wave_freq * x[i] * j)
            f_val += 0.7 * wave_sum
        
        # Modified radial basis functions with dynamic centers and widths
        for i in range(self.rbf_count):
            center = -4.5 + (9.0 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.3 + 0.7 * np.sin(i * 0.8)
            height = 1.2 + 0.8 * np.cos(i * 1.1)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with enhanced sine modulation
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = np.sin(0.7 * x[i]) * np.cos(0.4 * x[j])
            f_val += 0.5 * coupling
        
        # Asymmetric saddle points with modified exponential scaling
        for i in range(self.dim):
            if i % 2 == 0:
                f_val += 0.6 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.15 * x[i])
            else:
                f_val += 0.6 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.15 * x[i])
        
        # Additional high-frequency oscillatory component with adaptive amplitude
        for i in range(self.dim):
            amplitude = 0.4 + 0.3 * np.sin(i * 0.7)
            f_val += amplitude * np.sin(20.0 * x[i])
            
        # Chaotic coupling term to increase ruggedness
        chaotic_term = 0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i]) * np.cos(x[(i+2) % self.dim]) * np.sin(x[(i+4) % self.dim])
        f_val += 0.3 * chaotic_term
        
        return f_val