import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Create a more complex multimodal function with chaotic behavior
        # Combines polynomial terms with multiple sinusoidal components
        # and introduces chaotic perturbations for increased complexity
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(10 * x)) + 0.3 * np.sum(np.cos(7 * x)) + \
                 0.1 * np.sum(np.sin(3 * x)**2) + 0.05 * np.sum(x**6) + \
                 0.2 * np.sum(np.sin(15 * x) * np.cos(12 * x))
        
        # Add chaotic component using a logistic map-like behavior
        chaotic_term = 0.0
        for i in range(min(5, self.dim)):
            if i < len(x):
                chaotic_term += np.sin(x[i] * (i + 1) * 3.14159) * np.cos(x[i] * (i + 1) * 2.71828)
        
        result += 0.15 * chaotic_term
        
        return result