import numpy as np

class ProbabilisticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.0 * x))
        
        # Trigonometric oscillations with frequency modulation
        trig_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            trig_osc += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Basin attraction components with probabilistic weighting
        basin_attraction = 0.0
        for i in range(self.dim):
            # Each dimension has a probabilistic attraction center
            center = 2.0 * np.sin(i)
            distance = np.abs(x[i] - center)
            # Weighted by inverse of distance squared (with small offset to avoid division by zero)
            basin_attraction += 1.0 / (distance**2 + 0.1) * np.exp(-0.1 * distance)
        
        # Cross-dimensional interaction with Gaussian kernels
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist_ij = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_interaction += np.exp(-dist_ij**2) * np.sin(x[i] * x[j])
        
        # Polynomial and logarithmic components for additional complexity
        poly_term = np.sum(x**4) * np.log(np.abs(np.sum(x)) + 1.0)
        log_term = np.sum(np.log(np.abs(x) + 1.0))
        
        # Final combined function with dynamic scaling
        result = exp_decay + trig_osc + basin_attraction + cross_interaction + poly_term + log_term
        
        return result