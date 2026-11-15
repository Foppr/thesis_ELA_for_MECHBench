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
        
        # Trigonometric oscillations with varying frequencies
        trig_term = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x))
        
        # Exponential decay interaction terms
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                decay_interaction += np.exp(-distance / (1.0 + 0.1 * (i + j)))
        
        # Nested local minima structure
        nested_penalty = 0.0
        for k in range(1, min(6, self.dim + 1)):
            scale = 2.0 ** k
            loc = np.full(self.dim, 1.0 / scale)
            dist = np.sum((x - loc)**2)
            nested_penalty += np.exp(-dist / (2.0 * (k**2)))
        
        # Add chaotic perturbations
        chaotic = np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * np.exp(-0.5 * x**2))
        
        # Combine all components
        result = quadratic + 0.5 * trig_term + 0.1 * decay_interaction + 0.3 * nested_penalty + 0.2 * chaotic
        
        return result