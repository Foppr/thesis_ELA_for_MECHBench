import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components
        term1 = np.sum(x**2)
        term2 = 0.8 * np.sum(np.sin(7 * x) * np.cos(4 * x) * np.exp(-0.1 * np.abs(x)))
        term3 = 0.15 * np.sum(x**6 * np.sin(3 * x))
        term4 = 0.4 * np.sum(np.exp(-x**2) * np.sin(15 * x) * np.cos(5 * x))
        term5 = 0.08 * np.sum(np.abs(x) ** 4.2)
        term6 = 0.2 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Add complex interaction terms between dimensions
        interaction = 0.03 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(7 * (x[:-1] + x[1:])))
        interaction += 0.01 * np.sum((x[:-2] - x[2:]) ** 2 * np.cos(4 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component
        barrier = 0.5 * np.sum(np.exp(-0.5 * (x - np.mean(x))**2) * np.sin(20 * x))
        
        # Add novel cross-dimensional coupling terms
        cross_dim = 0.1 * np.sum(np.sin(2 * x) * np.cos(3 * x) * np.exp(-0.2 * np.abs(x)))
        cross_dim += 0.05 * np.sum(x**4 * np.sin(5 * x) * np.cos(2 * x))
        
        # Add a new chaotic component with multi-scale sinusoidal modulation
        chaotic = 0.3 * np.sum(np.sin(10 * x) * np.cos(8 * x) * np.exp(-0.3 * x**2))
        chaotic += 0.25 * np.sum(np.sin(12 * x) * np.cos(6 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Add a complex interaction between all dimensions
        complex_interaction = 0.02 * np.sum(np.prod(x[np.newaxis, :] - x[:, np.newaxis], axis=0) * np.sin(3 * np.sum(x)))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + cross_dim + chaotic + complex_interaction
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result