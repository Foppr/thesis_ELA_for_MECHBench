import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Exponentially decaying Gaussian peaks with varying widths and heights
        peaks = 0
        num_peaks = 20
        for i in range(num_peaks):
            # Randomly positioned peaks with exponential decay in width
            center = np.random.uniform(-1, 1, self.dim)
            width = 0.1 * np.exp(-0.1 * i)
            height = 1.0 + 0.5 * np.sin(i)
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - center) / width)**2))
        
        # Cross-dimensional coupling with sine and cosine interactions
        coupling = 0
        for i in range(self.dim - 1):
            coupling += np.sin(10 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i+1])
            coupling += np.cos(8 * np.pi * x_norm[i]) * np.sin(12 * np.pi * x_norm[i+1])
        
        # Fractional polynomial with non-integer exponents for additional complexity
        fractional = np.sum(np.abs(x_norm)**1.7 + np.abs(x_norm)**2.3)
        
        # Sharp transition regions using a combination of hyperbolic tangent functions
        transitions = 0
        for i in range(self.dim):
            transitions += np.tanh(10 * x_norm[i])**2 + np.tanh(5 * x_norm[i])**3
        
        # Combine components with different weights
        result = 0.3 * quadratic + 0.4 * peaks + 0.2 * coupling + 0.05 * fractional + 0.05 * transitions
        
        # Add noise proportional to the function value
        noise = 0.02 * (1 + np.abs(result)) * np.random.uniform(-1, 1)
        
        return result + noise