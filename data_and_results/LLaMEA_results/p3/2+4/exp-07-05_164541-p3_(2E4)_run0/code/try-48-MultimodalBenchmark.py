import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(10 * x) * np.exp(-0.1 * x**2) * np.cos(3 * x) * np.sin(7 * x))
        
        # Polynomial valley component with multiple roots and curvature changes
        valley_term = np.sum(0.3 * x**8 - 4 * x**6 + 7 * x**4 - 5 * x**2 + 2 * x)
        
        # Radial symmetry component with multiple peaks and valleys
        radial_term = np.sum((x**2).sum()**0.5 * np.cos(5 * np.sqrt(x**2).sum()) + 
                            np.sin(2 * np.sqrt(x**2).sum()) * np.cos(3 * np.sqrt(x**2).sum()))
        
        # Cross-dimensional interference with phase-shifted interactions
        interference_term = np.sum(np.sin(4 * x[:-1] + 2 * x[1:]) * np.cos(3 * x[:-1] - x[1:]) * 
                                 np.sin(5 * x[:-1] * x[1:]) + 
                                 np.cos(2 * x[:-1] * x[1:]) * np.sin(6 * x[:-1] + 3 * x[1:]))
        
        # Additional chaotic modulation with exponential decay
        mod_term = np.sum(np.exp(-0.2 * x**2) * np.sin(9 * x) * np.cos(4 * x) * np.sin(5 * x))
        
        # Combine all terms with optimized weights and add global offset
        return 0.3 * chaotic_term + 0.15 * valley_term + 0.2 * radial_term + 0.1 * interference_term + 0.05 * mod_term + 2.1