import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # High-dimensional chaotic multimodal components
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(5.0 * x)**2) + 0.3 * np.sum(np.cos(2.0 * x)**2)
        
        # Add polynomial distortion with chaotic coefficients
        poly_term = 0.01 * np.sum((x**3 + 0.5 * x**5) * np.sin(x))
        
        # Cross-dimensional coupling with chaotic interaction
        coupling = 0.2 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]))
        
        # Add chaotic perturbations
        chaotic = 0.1 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)))
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic
        
        return result