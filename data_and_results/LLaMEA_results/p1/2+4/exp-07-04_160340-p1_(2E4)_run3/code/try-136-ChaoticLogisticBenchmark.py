import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
        self.r = 3.9  # Chaos parameter for logistic map
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic component using logistic map iterations
        chaotic_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Initialize chaotic sequence
            logistic_val = 0.5
            # Iterate logistic map for several steps
            for _ in range(10):
                logistic_val = self.r * logistic_val * (1 - logistic_val)
            # Use chaotic value to modulate fitness
            chaotic_penalty += np.sin(10 * logistic_val) * np.cos(5 * logistic_val)
        
        # Add periodic modulation with varying frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            periodic_term += np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
        
        # Create a multi-scale, self-similar structure using recursive scaling
        scale_factor = 0.3
        recursive_penalty = 0.0
        for depth in range(1, 5):
            scaled_x = scale_factor**depth * x
            # Apply a nonlinear transformation
            transformed = np.sin(np.pi * scaled_x)
            recursive_penalty += np.sum(transformed**2) / (depth**1.5)
        
        # Add exponential decay interaction terms
        interaction_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x[i] - x[j])**2
                interaction_penalty += np.exp(-dist / (2.0 * (i + j + 1)**2))
        
        result += 0.5 * chaotic_penalty + 0.3 * periodic_term + 0.2 * recursive_penalty + 0.1 * interaction_penalty
        
        return result