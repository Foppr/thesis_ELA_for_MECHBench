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
        
        # Base polynomial term with varying degree
        f_val = np.sum(x**self.poly_degree)
        
        # Chaotic trigonometric wave interference pattern
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 6):
                wave_sum += np.sin(self.wave_freq * x[i] * j) * np.cos(self.wave_freq * x[i] * j)
            f_val += 0.7 * wave_sum
        
        # Dynamic radial basis functions with time-varying widths and heights
        for i in range(self.rbf_count):
            center = -4.5 + (9.0 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.3 + 0.7 * np.sin(i * 0.8 + np.pi/4)
            height = 1.5 + 0.5 * np.cos(i * 1.1 + np.pi/3)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            j = (i + 2) % self.dim
            coupling = np.sin(0.7 * x[i]) * np.cos(0.4 * x[j]) * np.sin(0.3 * x[i] * x[j])
            f_val += 0.4 * coupling
        
        # Asymmetric saddle points with multi-exponential scaling
        for i in range(self.dim):
            if i % 3 == 0:
                f_val += 0.6 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.15 * x[i]) * np.sin(0.5 * x[i])
            elif i % 3 == 1:
                f_val += 0.6 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.15 * x[i]) * np.cos(0.5 * x[i])
            else:
                f_val += 0.6 * (x[i]**3 - x[i]) * np.exp(-0.1 * x[i]**2)
        
        # High-frequency oscillatory component with dynamic amplitude and phase
        for i in range(self.dim):
            amplitude = 0.4 + 0.3 * np.sin(i * 0.6 + np.pi/2)
            phase = 0.2 * np.cos(i * 0.4)
            f_val += amplitude * np.sin(20.0 * x[i] + phase)
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 10.0) * np.cos(x[i] * 7.0) * np.tan(x[i] * 3.0)
        f_val += 0.2 * noise
        
        return f_val