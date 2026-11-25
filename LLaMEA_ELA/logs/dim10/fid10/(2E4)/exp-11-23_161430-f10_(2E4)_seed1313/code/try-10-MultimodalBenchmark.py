import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Core multimodal components with enhanced complexity
        result = np.sum(x**2) + 0.8 * np.sum(np.sin(12 * x)) + 0.6 * np.sum(np.cos(9 * x)) + \
                 0.4 * np.sum(np.sin(5 * x)**2) + 0.3 * np.sum(np.cos(8 * x)**2) + \
                 0.1 * np.sum(x**6) + 0.5 * np.sum(np.sin(18 * x) * np.cos(14 * x))
        
        # Enhanced chaotic perturbation with cross-dimensional interactions
        chaotic_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic_term += 0.4 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+2])
            elif i == self.dim - 2:
                chaotic_term += 0.3 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[0])
        
        # Additional symmetry-breaking terms
        symmetry_break = 0.2 * np.sum(np.sin(2 * x) * np.cos(3 * x)) + \
                         0.15 * np.sum(np.sin(4 * x)**3)
        
        result += chaotic_term + symmetry_break
        
        # Add a small Gaussian noise term to increase robustness
        noise = 0.01 * np.random.normal(0, 1, self.dim)
        result += np.sum(noise * x)
        
        return result