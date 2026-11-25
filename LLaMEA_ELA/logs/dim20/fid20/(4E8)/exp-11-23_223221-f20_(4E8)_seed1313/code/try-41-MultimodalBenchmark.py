import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp = 2 + int(i * 0.7) % 4  # Varying exponents: 2, 3, 4, 5
            poly_term += 0.1 * (x[i] ** exp)
        
        # Trigonometric coupling terms between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += 0.05 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j])
        
        # Adaptive noise component based on dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * (1 + 0.1 * i)
        
        # Cross-dimensional interaction with exponential decay
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interaction += 0.03 * np.exp(-dist) * np.sin(2 * x[i]) * np.cos(1.5 * x[j])
        
        # Global shaping term with sinusoidal modulation
        global_shape = 0.0
        for i in range(self.dim):
            global_shape += 0.04 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[i]) * (x[i]**2 + 1)
        
        return poly_term + trig_coupling + noise + interaction + global_shape