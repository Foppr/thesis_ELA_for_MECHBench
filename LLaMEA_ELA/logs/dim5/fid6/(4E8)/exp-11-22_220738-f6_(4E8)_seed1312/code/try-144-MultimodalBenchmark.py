import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 6
        self.wave_freq = 7.2
        self.rbf_count = min(12, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying degree
        f_val = np.sum(x**self.poly_degree)
        
        # Chaotic trigonometric wave interference pattern
        for i in range(self.dim):
            wave_sum = 0
            for j in range(1, 9):
                wave_sum += np.sin(self.wave_freq * x[i] * j) * np.cos(self.wave_freq * x[i] * j)
            f_val += 1.5 * wave_sum
        
        # Dynamic radial basis functions with time-varying widths and heights
        for i in range(self.rbf_count):
            center = -4.8 + (9.6 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.2 + 0.7 * np.sin(i * 0.9 + np.pi/4)
            height = 2.5 + 1.0 * np.cos(i * 1.3 + np.pi/5)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            j = (i + 4) % self.dim
            coupling = np.sin(1.3 * x[i]) * np.cos(0.7 * x[j]) * np.sin(0.6 * x[i] * x[j])
            f_val += 0.8 * coupling
        
        # Asymmetric saddle points with multi-exponential scaling
        for i in range(self.dim):
            if i % 5 == 0:
                f_val += 1.2 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.3 * x[i]) * np.sin(0.7 * x[i])
            elif i % 5 == 1:
                f_val += 1.2 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.3 * x[i]) * np.cos(0.7 * x[i])
            elif i % 5 == 2:
                f_val += 1.2 * (x[i]**3 - x[i]) * np.exp(-0.2 * x[i]**2)
            elif i % 5 == 3:
                f_val += 1.2 * (x[i]**4 - 2*x[i]**2 + 1) * np.exp(-0.15 * x[i]) * np.tan(0.4 * x[i])
            else:
                f_val += 1.2 * (x[i]**5 - x[i]**3) * np.exp(-0.1 * x[i]**2)
        
        # High-frequency oscillatory component with dynamic amplitude and phase
        for i in range(self.dim):
            amplitude = 0.8 + 0.6 * np.sin(i * 0.9 + np.pi/4)
            phase = 0.4 * np.cos(i * 0.7)
            f_val += amplitude * np.sin(30.0 * x[i] + phase)
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 14.0) * np.cos(x[i] * 10.0) * np.tan(x[i] * 5.0)
        f_val += 0.4 * noise
        
        # Add a hyperchaotic tent map component for enhanced ruggedness
        tent_map = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                tent_map += 0.6 * np.abs(x[i] - 2.8)
            elif i % 3 == 1:
                tent_map += 0.7 * np.abs(x[i] + 2.5)
            else:
                tent_map += 0.9 * np.abs(x[i] - 1.2)
        f_val += 0.5 * tent_map
        
        # Add adaptive scaling factor based on dimensionality
        adaptive_factor = 1.0 + 0.3 * np.sin(np.pi * self.dim / 10.0)
        f_val *= adaptive_factor
        
        return f_val