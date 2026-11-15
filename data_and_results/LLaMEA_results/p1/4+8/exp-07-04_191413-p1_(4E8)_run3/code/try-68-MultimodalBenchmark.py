import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic conditioning term
        quadratic = np.sum(x_scaled**2)
        
        # Logarithmic barrier terms to keep solution within bounds
        barrier = np.sum(-np.log(1.0 - x_scaled**2 + 1e-10))
        
        # Multiple Gaussian peaks with varying heights and positions
        peaks = 0.0
        peak_centers = np.linspace(-0.8, 0.8, 5)
        for center in peak_centers:
            peaks += np.exp(-5 * np.sum((x_scaled - center)**2))
        
        # Saddle-point structure with cross-dimensional coupling
        saddle = np.sum(x_scaled[:-1]**2 * x_scaled[1:]**2)
        
        # Sinusoidal modulation with varying frequency
        sin_mod = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 0.3 * barrier + 0.4 * peaks + 0.2 * saddle + 0.1 * sin_mod