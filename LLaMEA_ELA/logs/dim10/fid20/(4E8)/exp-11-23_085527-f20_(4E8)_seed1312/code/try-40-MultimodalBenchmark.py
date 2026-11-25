import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term with mixed powers
        polynomial = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6)
        
        # Trigonometric components with varying frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi
            amplitude = 1.0 / (1.0 + 0.1 * i)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i])
        
        # Exponential decay components with cross-terms
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(3 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i] + x_scaled[j])**2 * np.sin(2 * x_scaled[i] * x_scaled[j])
        
        # Global scaling and combination
        return 5.0 * polynomial + 3.0 * trigonometric + 2.0 * exponential + 1.5 * interaction