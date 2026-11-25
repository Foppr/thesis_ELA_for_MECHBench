import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component with varying degrees
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += (x[i] ** 4) / (1.0 + 0.1 * i) - 2.0 * (x[i] ** 2)
        
        # Gaussian peak component with adaptive heights and widths
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 1.0 + 0.5 * np.sin(0.5 * i)
            width = 0.5 + 0.3 * np.cos(0.3 * i)
            center = 2.0 * np.sin(0.4 * i)
            gaussian_term += height * np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Logarithmic barrier component creating sharp transitions
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += np.log(1.0 + np.exp(5.0 * (np.abs(x[i]) - 4.0)))
        
        # Cross-dimensional interaction with trigonometric coupling
        trig_coupling = 0.0
        for i in range(self.dim-1):
            trig_coupling += np.sin(x[i] * x[i+1]) * np.cos(0.5 * (x[i] + x[i+1]))
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return (valley_term + gaussian_term + barrier_term + trig_coupling) * scale_factor