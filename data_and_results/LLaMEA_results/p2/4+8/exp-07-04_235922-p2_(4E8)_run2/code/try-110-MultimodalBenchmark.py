import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic multimodal components with more complex interactions
        term1 = np.sum(x**2)
        term2 = 0.7 * np.sum(np.sin(9 * x) * np.cos(5 * x) * np.exp(-0.15 * np.abs(x)))
        term3 = 0.2 * np.sum(x**7 * np.sin(4 * x))
        term4 = 0.35 * np.sum(np.exp(-x**2) * np.sin(18 * x) * np.cos(6 * x))
        term5 = 0.1 * np.sum(np.abs(x) ** 4.5)
        term6 = 0.25 * np.sum(np.sin(x**4) * np.cos(x**3))
        
        # Add complex interaction terms between dimensions with higher-order coupling
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 4 * np.sin(8 * (x[:-1] + x[1:])))
        interaction += 0.02 * np.sum((x[:-2] - x[2:]) ** 3 * np.cos(5 * (x[:-2] + x[2:])))
        interaction += 0.015 * np.sum((x[:-3] - x[3:]) ** 2 * np.sin(6 * (x[:-3] + x[3:])))
        
        # Add a dynamic exponential barrier component with multi-scale modulation
        barrier = 0.6 * np.sum(np.exp(-0.3 * (x - np.mean(x))**2) * np.sin(25 * x) * np.cos(10 * x))
        
        # Add a multi-scale sinusoidal modulation component
        modulation = 0.15 * np.sum(np.sin(2 * x) * np.cos(3 * x) * np.sin(7 * x) * np.cos(9 * x))
        
        # Add a complex polynomial coupling term
        poly_coupling = 0.1 * np.sum((x**2 + x**3 + x**4) * np.sin(2 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + poly_coupling
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result