import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**8)
        
        # Trigonometric components with varying frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.1 * i)
            amplitude = 1.0 / (1.0 + 0.2 * i)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i])
        
        # Exponential decay components with cross-terms and adaptive scaling
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(5 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with higher-order coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i]**2 + x_scaled[j]**2)**2 * np.sin(3 * x_scaled[i] * x_scaled[j])
        
        # Additional cubic and quartic cross-terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x_scaled[i] * x_scaled[j])**3
        
        # Global scaling and combination
        return 4.0 * polynomial + 2.5 * trigonometric + 1.8 * exponential + 1.2 * interaction + 0.8 * cubic_interaction