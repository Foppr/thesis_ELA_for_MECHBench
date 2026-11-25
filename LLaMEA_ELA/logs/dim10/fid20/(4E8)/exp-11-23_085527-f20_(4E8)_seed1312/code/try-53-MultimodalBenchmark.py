import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed degrees and adaptive weights
        polynomial = np.sum((x_scaled**2 + 0.1 * x_scaled**4 + 0.01 * x_scaled**6))
        
        # Enhanced trigonometric components with dynamic frequencies
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i))
            amplitude = 1.0 / (1.0 + 0.2 * i)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Exponential cross-terms with variable coupling strength
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + 0.1 * (i + j))
                exp_term = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(coupling * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Dynamic conditioning based on distance from origin and dimensionality
        dist_from_origin = np.sqrt(np.sum(x_scaled**2))
        conditioning = 0.5 * (self.dim - 1) * dist_from_origin * np.log(1.0 + dist_from_origin)
        
        # Additional cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x_scaled[i]**3) * (x_scaled[j]**3) * np.cos(np.pi * (i + j))
        
        # Combine all components with optimized weights
        return 2.0 * polynomial + 3.0 * trigonometric + 1.5 * exponential + conditioning + 0.5 * cubic_interaction