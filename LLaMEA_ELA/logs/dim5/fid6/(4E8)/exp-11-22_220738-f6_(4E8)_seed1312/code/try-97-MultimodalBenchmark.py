import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 5
        self.wave_freq = 3.0
        self.rbf_count = min(7, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with variable exponent
        f_val = np.sum(x**self.poly_degree)
        
        # Chaotic wave interference with time-varying frequencies
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 6):
                freq = self.wave_freq * (1 + 0.3 * np.sin(i * 0.7 + j))
                wave_sum += np.sin(freq * x[i] * j) * np.cos(freq * x[i] * j)
            f_val += 0.4 * wave_sum
        
        # Adaptive RBFs with non-uniform centers and dynamic scaling
        for i in range(self.rbf_count):
            center = -4.5 + (9.0 * i**1.5) / (self.rbf_count**1.5) if self.rbf_count > 1 else 0.0
            width = 0.3 + 0.7 * np.sin(i * 0.8 + 1.2)
            height = 1.5 + 0.8 * np.cos(i * 1.1 + 0.9)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional cubic coupling with phase modulation
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = np.sin(0.4 * x[i])**3 * np.cos(0.2 * x[j])**3
            f_val += 0.25 * coupling
        
        # Asymmetric saddle points with exponential scaling and dynamic offsets
        for i in range(self.dim):
            offset = 0.5 * np.sin(i * 0.6)
            if i % 3 == 0:
                f_val += 0.3 * (x[i]**2 - 2*x[i] + 1 + offset) * np.exp(-0.15 * x[i])
            elif i % 3 == 1:
                f_val += 0.3 * (x[i]**2 + 2*x[i] + 1 + offset) * np.exp(0.15 * x[i])
            else:
                f_val += 0.3 * (x[i]**3 - 3*x[i] + offset) * np.exp(-0.05 * x[i]**2)
        
        # High-frequency oscillatory component with adaptive amplitude and phase
        for i in range(self.dim):
            amplitude = 0.4 + 0.3 * np.sin(i * 0.8 + 1.5)
            phase = 0.2 * np.cos(i * 0.6 + 0.9)
            f_val += amplitude * np.sin(20.0 * x[i] + phase)
            
        # Add a chaotic attractor component with logistic map modulation
        logistic_input = 3.8 * (x[0] / 5.0) * (1 - x[0] / 5.0) if self.dim > 0 else 0
        f_val += 0.2 * np.sin(logistic_input * 10) * np.cos(logistic_input * 7)
        
        return f_val