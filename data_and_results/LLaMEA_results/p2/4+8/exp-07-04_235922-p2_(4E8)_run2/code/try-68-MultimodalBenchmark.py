import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified frequencies
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(9 * x) * np.cos(5 * x))  # Increased frequencies
        term3 = 0.18 * np.sum(x**6 * np.sin(4 * x))  # Adjusted polynomial coupling
        term4 = 0.35 * np.sum(np.exp(-0.4 * x**2) * np.sin(17 * x))  # Modified decay and frequency
        term5 = 0.09 * np.sum(np.abs(x) ** 4.5)  # Slightly altered power
        
        # Enhanced interaction terms between dimensions with different power
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(8 * (x[:-1] + x[1:])))  # Higher order interaction
        
        # Add cross-dimensional polynomial coupling with different coefficients
        cross_term = 0.06 * np.sum(x[:-1] * x[1:] * np.sin(5 * (x[:-1]**2 + x[1:]**2)))  # Modified frequency
        
        # Add adaptive exponential decay barriers with different parameters
        barrier = 0.25 * np.sum(np.exp(-2.5 * np.abs(x)) * np.cos(9 * x))  # Modified barrier parameters
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_term + barrier
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result