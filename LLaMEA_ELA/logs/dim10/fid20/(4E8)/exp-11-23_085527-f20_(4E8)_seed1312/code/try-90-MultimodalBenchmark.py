import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**6)
        
        # Enhanced trigonometric components with variable frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(i * 0.5))
            amplitude = 1.0 / (1.0 + 0.4 * i)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i])
        
        # Exponential decay components with stronger cross-terms
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(7 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with cubic components and modified weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i]**3 + x_scaled[j]**3) * np.sin(4 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms for increased complexity
        quadratic = 0.7 * np.sum(x_scaled**2)
        cubic = 0.2 * np.sum(x_scaled**3)
        
        # Global scaling and combination
        return 5.0 * polynomial + 3.0 * trigonometric + 2.2 * exponential + 1.7 * interaction + 1.0 * quadratic + 0.4 * cubic