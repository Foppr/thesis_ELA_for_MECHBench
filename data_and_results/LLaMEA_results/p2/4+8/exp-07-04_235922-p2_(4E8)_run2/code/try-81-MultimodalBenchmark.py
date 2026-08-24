import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with modified coefficients
        term1 = np.sum(x**2)
        term2 = 0.9 * np.sum(np.sin(8 * x) * np.cos(3 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.2 * np.sum(x**6 * np.sin(2.5 * x))
        term4 = 0.35 * np.sum(np.exp(-x**2) * np.sin(16 * x) * np.cos(4 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        term6 = 0.25 * np.sum(np.sin(x**3) * np.cos(x**2))
        
        # Add complex interaction terms between dimensions with modified weights
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 3 * np.sin(6 * (x[:-1] + x[1:])))
        interaction += 0.015 * np.sum((x[:-2] - x[2:]) ** 2 * np.cos(3.5 * (x[:-2] + x[2:])))
        
        # Add a dynamic exponential barrier component with altered parameters
        barrier = 0.6 * np.sum(np.exp(-0.4 * (x - np.mean(x))**2) * np.sin(18 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result