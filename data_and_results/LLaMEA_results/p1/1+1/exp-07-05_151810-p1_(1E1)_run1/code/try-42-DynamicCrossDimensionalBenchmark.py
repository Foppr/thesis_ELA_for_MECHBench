import numpy as np

class DynamicCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with dynamic coefficients
        poly_base = np.sum((0.5 + 0.5 * np.sin(0.3 * np.arange(self.dim))) * x**2)
        
        # Trigonometric cross-dimensional coupling with dynamic frequencies
        freqs = 1.0 + 2.0 * np.abs(np.sin(0.4 * np.arange(self.dim)))
        trig_coupling = np.sum(np.sin(freqs * x) * np.cos(freqs * x) * 
                              np.exp(-0.1 * np.abs(x)) * 
                              np.sin(0.5 * np.sum(x) + np.pi/4))
        
        # Exponential barrier with adaptive width
        barrier_width = 1.0 + 0.5 * np.cos(0.2 * np.arange(self.dim))
        exp_barrier = np.sum(np.exp(-0.5 * (x / barrier_width)**2) * 
                            np.cos(0.3 * x) * 
                            np.sin(0.7 * x))
        
        # Multi-scale oscillatory component with frequency modulation
        scale_freqs = 0.5 + 1.5 * np.sin(0.6 * np.arange(self.dim))
        oscillatory = np.sum(np.sin(scale_freqs * x**2) * 
                            np.cos(scale_freqs * x) * 
                            np.exp(-0.2 * np.abs(x)))
        
        # Cross-dimensional interaction with weighted distance
        dist_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist_interaction += (x[i] - x[j])**2 * np.exp(-0.1 * np.abs(x[i] + x[j]))
        
        # Adaptive power scaling with dimension-dependent exponents
        exponents = 1.0 + 0.5 * np.sin(0.4 * np.arange(self.dim))
        power_scaling = np.sum(np.abs(x)**exponents)
        
        # Combined result
        result = poly_base + trig_coupling + exp_barrier + oscillatory + dist_interaction + power_scaling
        
        return result