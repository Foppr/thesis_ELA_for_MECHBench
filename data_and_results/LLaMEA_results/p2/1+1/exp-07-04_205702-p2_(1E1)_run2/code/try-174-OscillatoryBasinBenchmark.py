import numpy as np

class OscillatoryBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        f1 = 0.3 * np.sum(x**2)
        
        # Multiple oscillatory peaks with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(min(6, self.dim)):
            freq = 2.0 + 1.5 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            phase = 0.5 * np.pi * np.sin(0.4 * i)
            f2 -= amp * np.cos(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric basins with exponential and trigonometric components
        f3 = 0.0
        for i in range(self.dim):
            f3 += 0.5 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(1.5 * x[i]) + \
                  0.3 * np.exp(-0.1 * (x[i] + 1.5)**2) * np.cos(2.0 * x[i])
        
        # Cross-dimensional interaction terms with sine and cosine products
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f4 += 0.2 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
        
        # Gradient variation through fractional powers and logarithmic terms
        f5 = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                f5 += 0.1 * np.abs(x[i])**1.7 * np.log(np.abs(x[i]) + 1.0)
        
        # Multi-modal structure with multiple local minima
        f6 = 0.0
        for i in range(self.dim):
            f6 += 0.4 * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i]) + \
                  0.3 * np.sin(2.0 * x[i]) * np.cos(1.0 * x[i])
        
        # Add noise for robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise