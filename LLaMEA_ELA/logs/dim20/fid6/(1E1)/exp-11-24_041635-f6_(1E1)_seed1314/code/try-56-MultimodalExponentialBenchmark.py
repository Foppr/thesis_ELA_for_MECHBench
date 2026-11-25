import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and oscillation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(2.0 * r)
        
        # Multimodal trigonometric components with varying frequencies
        modal_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            modal_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.05 * (x[i]**2))
        
        # Cross-dimensional interaction with adaptive scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.abs(x[i] - x[j])
                cross_term += np.exp(-dist) * np.sin(1.5 * (x[i] + x[j]))
        
        # Polynomial and logarithmic components for additional complexity
        poly_term = np.sum(x**4) * 0.01
        log_term = np.sum(np.log(1.0 + 0.1 * x**2)) * 0.5
        
        # Final multimodal combination with dimensionality scaling
        result = radial_term + modal_sum + cross_term + poly_term + log_term
        
        return result