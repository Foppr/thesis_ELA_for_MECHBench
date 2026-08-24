import numpy as np

class SinusoidalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create highly multimodal landscape with exponential frequency growth
        result = 0.0
        for i in range(self.dim):
            # Add exponentially increasing sinusoidal components
            freq = 2 ** (i + 1)
            result += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i] / 2)
            # Add higher-order polynomial terms for conditioning
            result += 0.05 * x_norm[i]**4
            # Add complex interaction terms with exponential coupling
            for j in range(i+1, self.dim):
                coupling = 2 ** (i + j)
                result += 0.03 * np.sin(coupling * np.pi * (x_norm[i] + x_norm[j])) * np.cos(coupling * np.pi * (x_norm[i] - x_norm[j]))
                # Add cross-dimensional polynomial interactions
                result += 0.02 * (x_norm[i]**2) * (x_norm[j]**3)
        
        # Add a complex global minimum landscape with multiple basins
        result += 0.3 * np.sum(np.abs(x_norm)**3)
        result += 0.1 * np.sum(np.sin(5 * np.pi * x_norm))
        
        return result