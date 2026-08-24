import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Add periodic sinusoidal components with varying frequencies
        sinusoidal = 0.0
        for i in range(1, self.dim + 1):
            sinusoidal += np.sin(i * x) * np.cos(i * x)
        
        # Exponential decay interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interaction += np.exp(-dist / (1.0 + i + j)) * np.sin(dist)
        
        # Add nested local minima using radial basis functions
        nested_penalty = 0.0
        centers = np.array([[0.5, -0.5], [-0.5, 0.5], [0.7, -0.7], [-0.7, 0.7]])
        if self.dim >= 2:
            for center in centers:
                if len(center) <= self.dim:
                    dist = np.sum((x[:2] - center)**2)
                    nested_penalty += np.exp(-dist / 0.5) * (1.0 + 0.5 * np.sin(dist))
        
        # Combine all components
        result = quadratic + 0.5 * sinusoidal + 0.1 * interaction + 0.2 * nested_penalty
        
        return result