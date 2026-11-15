import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with improved interaction
        term1 = np.sum(x**2)
        term2 = 0.7 * np.sum(np.sin(5 * x) * np.cos(3 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.2 * np.sum(x**5 * np.sin(2 * x))
        term4 = 0.3 * np.sum(np.exp(-x**2) * np.sin(12 * x) * np.cos(4 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 3.8)
        term6 = 0.15 * np.sum(np.sin(x**4) * np.cos(x**3))
        
        # Add complex interaction terms between dimensions with different weights
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(6 * (x[:-1] + x[1:])))
        interaction += 0.02 * np.sum((x[:-2] - x[2:]) ** 3 * np.cos(5 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component with modified parameters
        barrier = 0.4 * np.sum(np.exp(-0.3 * (x - np.mean(x))**2) * np.sin(18 * x))
        
        # Add a new component with higher-order polynomial and sinusoidal coupling
        coupling = 0.25 * np.sum(np.sin(x**2) * np.cos(x**3) * np.exp(-0.2 * np.abs(x)))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result