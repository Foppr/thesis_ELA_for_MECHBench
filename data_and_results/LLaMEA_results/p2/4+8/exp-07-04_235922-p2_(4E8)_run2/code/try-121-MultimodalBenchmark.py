import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation components
        term1 = np.sum(np.sin(5 * x) * np.cos(3 * x))
        term2 = np.sum(np.sin(2 * x) * np.cos(7 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Polynomial conditioning with adaptive exponents
        exponents = 2 + 3 * np.sin(np.arange(self.dim) * 0.5)
        term3 = np.sum(np.abs(x) ** exponents)
        
        # Radial barrier with dynamic center
        centers = np.sin(np.arange(self.dim) * 0.3) * 3.0
        distances = np.sqrt(np.sum((x - centers)**2, axis=0, keepdims=True))
        barrier = np.sum(np.exp(-0.5 * distances**2) * np.sin(10 * distances))
        
        # Coupling between dimensions with trigonometric modulation
        coupling = 0.05 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Higher-order polynomial interactions
        poly_interaction = 0.02 * np.sum((x[:-1] * x[1:]) ** 3)
        
        # Adaptive noise injection
        noise = 0.01 * np.sum(np.sin(13 * x) * np.cos(8 * x))
        
        result = term1 + term2 + term3 + barrier + coupling + poly_interaction + noise
        
        return result