import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial term with higher-order polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        
        # Enhanced radial oscillation with multiple frequencies
        radial_osc = np.sin(15 * r) * np.cos(8 * r) * np.sin(3 * r)
        
        # Cross-dimensional interaction terms
        cross_term = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Polynomial oscillation in each dimension with varying coefficients
        dim_osc = np.sum((np.sin(4 * np.pi * x_norm) ** 2) * (1 + 0.5 * np.abs(x_norm)))
        
        # Complex exponential barrier with multiple peaks near boundary
        barrier = np.sum(np.exp(-5 * (1 - np.abs(x_norm))**4) + 0.5 * np.exp(-2 * (1 - np.abs(x_norm))**2))
        
        # Additional high-frequency noise term
        noise = 0.1 * np.sum(np.sin(20 * x_norm) ** 2)
        
        # Combine all terms with adaptive weights
        return r**5 + 0.7 * radial_osc + 0.4 * cross_term + 0.3 * dim_osc + 0.2 * barrier + noise