import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Higher-order polynomial terms for increased curvature and complexity
        poly_term = np.sum(0.8 * x_normalized**6 + 0.5 * x_normalized**4 + 0.2 * x_normalized**3 + 0.1 * x_normalized**2)
        
        # Enhanced sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(1.5 * np.sin(15 * np.pi * x_normalized) + 0.8 * np.sin(7 * np.pi * x_normalized) + 0.3 * np.cos(12 * np.pi * x_normalized))
        
        # Modified exponential decay with varying rates to create complex shallow regions
        exp_term = np.sum(np.exp(-x_normalized**2 / 1.5) + np.exp(-x_normalized**2 / 0.5) - 2.0)
        
        # Cross-dimensional coupling with interaction strength that varies by dimension
        coupling_term = 0.4 * np.sum(x_normalized[:-1]**2 * x_normalized[1:] + x_normalized[:-1] * x_normalized[1:]**2)
        
        # Additional quadratic coupling between all pairs of dimensions for increased complexity
        quadratic_coupling = 0.1 * np.sum((x_normalized.reshape(-1, 1) - x_normalized.reshape(1, -1))**2)
        
        # Combine all terms
        return poly_term + sin_term + exp_term + coupling_term + quadratic_coupling