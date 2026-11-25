import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 7
        self.wave_freq = 6.5
        self.rbf_count = min(10, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying degree
        f_val = np.sum(x**self.poly_degree)
        
        # Chaotic trigonometric wave interference pattern
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 8):
                wave_sum += np.sin(self.wave_freq * x[i] * j) * np.cos(self.wave_freq * x[i] * j)
            f_val += 1.3 * wave_sum
        
        # Dynamic radial basis functions with time-varying widths and heights
        for i in range(self.rbf_count):
            center = -4.8 + (9.6 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.15 + 0.85 * np.sin(i * 0.8 + np.pi/3)
            height = 2.2 + 0.9 * np.cos(i * 1.2 + np.pi/4)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            j = (i + 3) % self.dim
            coupling = np.sin(1.2 * x[i]) * np.cos(0.6 * x[j]) * np.sin(0.5 * x[i] * x[j])
            f_val += 0.7 * coupling
        
        # Asymmetric saddle points with multi-exponential scaling
        for i in range(self.dim):
            if i % 4 == 0:
                f_val += 1.1 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.25 * x[i]) * np.sin(0.6 * x[i])
            elif i % 4 == 1:
                f_val += 1.1 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.25 * x[i]) * np.cos(0.6 * x[i])
            elif i % 4 == 2:
                f_val += 1.1 * (x[i]**3 - x[i]) * np.exp(-0.15 * x[i]**2)
            else:
                f_val += 1.1 * (x[i]**4 - 2*x[i]**2 + 1) * np.exp(-0.1 * x[i]) * np.tan(0.3 * x[i])
        
        # High-frequency oscillatory component with dynamic amplitude and phase
        for i in range(self.dim):
            amplitude = 0.7 + 0.5 * np.sin(i * 0.8 + np.pi/3)
            phase = 0.3 * np.cos(i * 0.6)
            f_val += amplitude * np.sin(25.0 * x[i] + phase)
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 13.0) * np.cos(x[i] * 9.0) * np.tan(x[i] * 4.5)
        f_val += 0.35 * noise
        
        # Add modified hyperchaotic component using logistic map instead of tent map
        logistic_map = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                logistic_map += 0.55 * (4.0 * x[i] * (1 - x[i]))  # Logistic map
            else:
                logistic_map += 0.85 * (3.8 * x[i] * (1 - x[i]))  # Another logistic map variant
        f_val += 0.45 * logistic_map
        
        # Add adaptive scaling factor based on dimensionality
        adaptive_factor = 1.0 + 0.25 * np.sin(np.pi * self.dim / 8.0)
        f_val *= adaptive_factor
        
        return f_val