import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric components with varying frequencies
        term1 = np.sum(np.sin(2 * np.pi * x) ** 2 + np.cos(2 * np.pi * x) ** 2)
        term2 = 0.5 * np.sum(np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x))
        term3 = 0.3 * np.sum(np.sin(7 * np.pi * x) ** 3)
        
        # Rational polynomial interactions
        poly_interaction = 0.2 * np.sum((x**2 + 1) / (x**2 + 0.5) - 1)
        
        # Adaptive gradient-based attraction fields
        attraction = 0.1 * np.sum((x - np.mean(x))**2 * np.exp(-0.1 * np.abs(x - np.mean(x))))
        
        # Nested multimodal structure with varying scales
        nested = 0.4 * np.sum(np.sin(10 * x) * np.exp(-0.05 * x**2))
        
        # Cross-dimensional coupling with rational weights
        coupling = 0.05 * np.sum((x[:-1] * x[1:] + 1) / (x[:-1]**2 + x[1:]**2 + 1))
        
        # Add a global scaling factor to control difficulty
        scaling = 1.0 + 0.1 * np.sin(np.sum(x**2) / self.dim)
        
        result = scaling * (term1 + term2 + term3 + poly_interaction + attraction + nested + coupling)
        
        # Add small random perturbation for increased robustness
        result += 0.0001 * np.random.random()
        
        return result