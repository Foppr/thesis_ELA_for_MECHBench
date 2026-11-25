import numpy as np

class ComplexMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Base polynomial term with varying exponents
        result = np.sum(x**4 + 0.5 * x**3 + 0.2 * x**2)
        
        # Add trigonometric interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a sinusoidal pattern that varies with dimension
        for i in range(self.dim):
            result += 2 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add random perturbations to increase complexity
        np.random.seed(42)  # For reproducibility
        noise = np.random.normal(0, 0.1, self.dim)
        result += np.sum(noise * x)
        
        # Add coupling between all dimensions through a global term
        result += 0.5 * np.sin(np.sum(x)) * np.cos(np.sum(x**2))
        
        # Scale and shift to ensure proper conditioning
        result = result * (1 + 0.2 * np.sum(np.abs(x_norm)))
        
        return result