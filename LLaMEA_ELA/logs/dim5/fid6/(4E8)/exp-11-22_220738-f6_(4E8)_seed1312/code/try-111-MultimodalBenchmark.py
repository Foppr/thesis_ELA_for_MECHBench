import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 7
        self.wave_freq = 5.0
        self.rbf_count = min(11, dim)
        
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
            f_val += 1.2 * wave_sum
        
        # Dynamic radial basis functions with time-varying widths and heights
        for i in range(self.rbf_count):
            center = -4.8 + (9.6 * i) / (self.rbf_count - 1) if self.rbf_count > 1 else 0.0
            width = 0.2 + 0.8 * np.sin(i * 0.9 + np.pi/3)
            height = 2.0 + 0.6 * np.cos(i * 1.3 + np.pi/4)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            j = (i + 3) % self.dim
            coupling = np.sin(0.9 * x[i]) * np.cos(0.5 * x[j]) * np.sin(0.4 * x[i] * x[j])
            f_val += 0.6 * coupling
        
        # Asymmetric saddle points with multi-exponential scaling
        for i in range(self.dim):
            if i % 4 == 0:
                f_val += 1.0 * (x[i]**2 - 2*x[i] + 1) * np.exp(-0.2 * x[i]) * np.sin(0.7 * x[i])
            elif i % 4 == 1:
                f_val += 1.0 * (x[i]**2 + 2*x[i] + 1) * np.exp(0.2 * x[i]) * np.cos(0.7 * x[i])
            elif i % 4 == 2:
                f_val += 1.0 * (x[i]**3 - x[i]) * np.exp(-0.15 * x[i]**2)
            else:
                f_val += 1.0 * (x[i]**4 - 2*x[i]**2 + 1) * np.exp(-0.1 * x[i]) * np.tan(0.6 * x[i])
        
        # High-frequency oscillatory component with dynamic amplitude and phase
        for i in range(self.dim):
            amplitude = 0.6 + 0.4 * np.sin(i * 0.7 + np.pi/3)
            phase = 0.3 * np.cos(i * 0.5)
            f_val += amplitude * np.sin(25.0 * x[i] + phase)
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 12.0) * np.cos(x[i] * 9.0) * np.tan(x[i] * 4.0)
        f_val += 0.3 * noise
        
        # Add irregularity through fractional polynomial terms
        for i in range(self.dim):
            f_val += 0.5 * np.sin(x[i] * 15.0) * x[i]**(1.7 + 0.3 * np.sin(i))
            
        return f_val