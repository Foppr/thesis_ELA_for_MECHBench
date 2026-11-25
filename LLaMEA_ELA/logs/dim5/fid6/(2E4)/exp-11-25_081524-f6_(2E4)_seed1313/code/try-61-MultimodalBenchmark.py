import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees
        poly_terms = np.sum(x**4 + 0.3 * x**6 + 0.1 * x**8)
        
        # Trigonometric oscillations with frequency modulation
        trig_terms = np.sum(np.sin(2.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic barrier near boundaries to encourage boundary handling
        log_barrier = np.sum(1.0 / (1.0 + np.exp(-x + 5.0)) + 1.0 / (1.0 + np.exp(x + 5.0)))
        
        # Asymmetric conditioning: different weights for positive and negative components
        pos_condition = np.sum(np.maximum(x, 0)**2 * (1.0 + 0.5 * np.sin(x)))
        neg_condition = np.sum(np.minimum(x, 0)**2 * (1.0 + 0.3 * np.cos(x)))
        
        # Clustered peaks with Gaussian-like attractions
        peak_attractors = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                peak_attractors += np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i+1] - 2.0)**2))
                peak_attractors += np.exp(-0.5 * ((x[i] + 2.0)**2 + (x[i+1] + 2.0)**2))
        
        # Cross-dimensional coupling with sine-based interactions
        cross_coupling = 0.5 * np.sum(np.sin(0.5 * (x[:-1] + x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Sharp gradients through hyperbolic tangent modulation
        tanh_modulation = np.sum(np.tanh(3.0 * x) * np.cos(4.0 * x))
        
        return poly_terms + trig_terms + log_barrier + pos_condition + neg_condition + peak_attractors + cross_coupling + tanh_modulation