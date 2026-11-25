import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Create a highly multimodal function with chaotic behavior
        # Combines polynomial terms with multiple sinusoidal components
        # and a chaotic logistic map component for increased complexity
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(10 * x)) + 0.3 * np.sum(np.cos(7 * x)) + \
                 0.1 * np.sum(np.sin(3 * x)**2) + 0.2 * np.sum(np.cos(5 * x)**2) + \
                 0.05 * np.sum(x**6) + 0.4 * np.sum(np.sin(15 * x) * np.cos(12 * x))
        
        # Add chaotic perturbation term
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += 0.3 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
        
        result += chaotic_term
        
        return result