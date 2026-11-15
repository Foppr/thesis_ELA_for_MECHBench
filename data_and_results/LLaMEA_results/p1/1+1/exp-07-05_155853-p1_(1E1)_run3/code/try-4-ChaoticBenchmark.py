import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 2.0 + i * 0.5
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Polynomial potential with asymmetric wells
        poly_component = 0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric cubic polynomial with different behavior on positive and negative sides
            if xi >= 0:
                poly_component += 0.5 * xi**3 + 0.3 * xi**2
            else:
                poly_component += 0.3 * xi**3 + 0.5 * xi**2
        
        # Chaotic interaction terms using logistic map-like behavior
        chaotic_component = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_component += 0.1 * np.sin(x[i] * x[i+1]) * (1.0 - x[i]**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.05 * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(2.0 * (x[i] + x[j]))
        
        # Global scaling and offset to ensure proper fitness range
        return 2.0 * sin_component + 1.5 * poly_component + 0.5 * chaotic_component + 0.3 * coupling + 5.0 * np.sum(x**4)