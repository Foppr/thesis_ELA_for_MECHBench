import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like components with logarithmic barriers
        term1 = np.sum(np.log(np.abs(x) + 1.0) * np.sin(5 * x))
        
        # Trigonometric coupling between dimensions
        term2 = 0.5 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        # Power-law interactions with fractal scaling
        power_interaction = 0.3 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.7)
        
        # Logarithmic barrier terms to create irregularity
        barrier = 0.2 * np.sum(np.log(1.0 + np.abs(x)) ** 2)
        
        # Combined fractal and chaotic behavior
        fractal_term = 0.1 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1.0)))
        
        result = term1 + term2 + power_interaction + barrier + fractal_term
        
        # Add small random perturbation to increase challenge
        result += 0.0005 * np.random.random()
        
        return result